import concurrent.futures
class Solution:
    def getHostname(self, url: str) -> str:
        # assume URLs are valid
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        s = set()
        s.add(startUrl)
        hostname = self.getHostname(startUrl)
        queue = [startUrl]
        while len(queue) > 0:
            queue2 = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                l = list(executor.map(lambda url: htmlParser.getUrls(url), queue))
                for urls in l:
                    for newUrl in urls:
                        if newUrl in s or self.getHostname(newUrl) != hostname:
                            continue
                        s.add(newUrl)
                        queue2.append(newUrl)
            queue = queue2
        return list(s)

