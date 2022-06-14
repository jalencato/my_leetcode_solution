import collections


class Solution:
    def findparents(self, graph):
        parent = collections.defaultdict(list)
        maxnode = -1
        for par, chi in graph:
            parent[chi].append(par)
            maxnode = max(par, chi)
        res = []
        for i in range(1, maxnode + 1):
            if len(parent[i]) == 1 or len(parent[i]) == 0:
                res.append(i)
        return res

    def findcommonancester(self, graph, node1, node2):
        parent = collections.defaultdict(list)
        for par, chi in graph:
            parent[chi].append(par)

        def ancestor_list(node):
            s = set()
            for k in parent[node]:
                s.add(k)
                par_par = ancestor_list(k)
                for k2 in par_par:
                    s.add(k2)
            return s

        return True if ancestor_list(node1) & ancestor_list(node2) else False

    def findfarthest(self, graph, node):
        parent = collections.defaultdict(list)
        for par, chi in graph:
            parent[chi].append(par)

        queue = [(node, 0)]
        print(queue)
        maxcnt, maxnode = -1, []
        while queue:
            tmp, cnt = queue.pop()
            # print(tmp, cnt)
            for n in parent[tmp]:
                queue.append((n, cnt + 1))
                if maxcnt < cnt + 1:
                    maxnode = []
                    maxnode.append(n)
                    maxcnt = cnt + 1
                elif maxcnt == cnt + 1:
                    maxnode.append(n)
        return maxnode

if __name__ == '__main__':
    graph = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
    s = Solution()
    # print(s.findparents(graph))
    # print(s.findcommonancester(graph, 6, 7))
    print(s.findfarthest(graph, 5))
