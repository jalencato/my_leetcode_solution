"""
object CrawlerHelper {
    private val htmlMap = mapOf(
            "1" to "2/3/4",
            "2" to "3/4",
            "3" to "5",
            "4" to "5",
            "5" to "6"
    )

    fun fetch(url: String): HTML {
        return HTML(htmlMap[url] ?: "")
    }

    fun parse(html: HTML): List<String> {
        return html.html.split("/").filter { it.isNotEmpty() }
    }

    fun save(url: String, html: HTML) {
        Thread.sleep(1000)
        println("url $url is saved")
    }
}

// BFS through the urls
// the bottleneck is at I/O operations
// time complexity: O(N)
// space complexity: O(N)
class WebCrawler {
    fun crawl(startUrl: String, depth: Int) {
        val queue: Queue<UrlEntry> = LinkedList()
        val visited = mutableSetOf(startUrl)

        queue.offer(UrlEntry(startUrl, 1))

        while (queue.isNotEmpty()) {
            val curUrlEntry = queue.poll()

            // I/O blocking
            val curHtml = CrawlerHelper.fetch(curUrlEntry.url)
            CrawlerHelper.save(curUrlEntry.url, curHtml)

            if (curUrlEntry.depth >= depth) continue

            val nextUrls = CrawlerHelper.parse(curHtml)
            nextUrls.forEach { url ->
                if (!visited.contains(url)) {
                    visited.add(url)
                    queue.offer(UrlEntry(url, curUrlEntry.depth + 1))
                }
            }
        }

    }
}

data class UrlEntry(val url: String, val depth: Int)

data class HTML(val html: String)
"""

"""
/**
 * improve the efficiency by multi-thread
 * keys
 * 1 - avoid race condition where 2 threads check same url
 * and try to process as next url at same time (this causes duplicate visit on same url)
 * use concurrentHashMap put to avoid, since the put (insert entry) lock the segment of map
 * and if return null meaning no such key in map previously which means we can process the url
 *
 * 2 - save is a disk I/O where we should put it into a separate thread pool to let it finish by itself
 * 3 - fetch html is a network I/O
 *
 */
class WebCrawlerMultiThread {
    fun crawl(startUrl: String, depth: Int) {
        val visited = ConcurrentHashMap<String, String>()
        val crawlerThreadExecutor = Executors.newFixedThreadPool(THREAD_POOL_MAX_SIZE)
                as ThreadPoolExecutor
        val saveThreadExecutor = Executors.newFixedThreadPool(THREAD_POOL_MAX_SIZE)
                as ThreadPoolExecutor

        val rootCrawlerFuture = crawlerThreadExecutor.submit(InnerCrawler(
                visited,
                crawlerThreadExecutor,
                saveThreadExecutor,
                startUrl,
                1,
                depth
        ))

        rootCrawlerFuture.get()
        crawlerThreadExecutor.shutdown()
        println("====crawler finished===")
        saveThreadExecutor.shutdown()
    }

    class InnerCrawler(
            private val visited: ConcurrentHashMap<String, String>,
            private val executor: ThreadPoolExecutor,
            private val diskWriteExecutor: ThreadPoolExecutor,
            private val url: String,
            private val curDepth: Int,
            private val maxDepth: Int
    ) : Runnable {
        private val nextCrawlers = mutableListOf<Future<*>>()

        override fun run() {
            val html = CrawlerHelper.fetch(url)

            diskWriteExecutor.submit { CrawlerHelper.save(url, html) }

            if (curDepth >= maxDepth) return

            val nextUrls = CrawlerHelper.parse(html)
            nextUrls.forEach { nextUrl ->
                // concurrentHashMap put will lock the map and only current thread can access
                // if return null meaning no same url in the map, thus safe to proceed
                if (visited.put(nextUrl, "") == null) {
                    nextCrawlers.add(executor.submit(InnerCrawler(
                            visited,
                            executor,
                            diskWriteExecutor,
                            nextUrl,
                            curDepth + 1,
                            maxDepth
                    )))
                }
            }

            // wait for subthreads to finish
            nextCrawlers.forEach { it.get() }
        }
    }

    companion object {
        private const val THREAD_POOL_MAX_SIZE = 8
    }
}
"""