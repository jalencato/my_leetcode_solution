import sys
import heapq

def dijkstra(graph):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[0] = 0  # 自己和自己距离为 0
    visited = set()

    min_heap = [(0, 0)]

    for _ in range(n):
        # 找到还没确定的里面距离最小的
        _, min_index = heapq.heappop(min_heap)
        # 已经确定了
        visited.add(min_index)
        for v in range(n):
            if v not in visited and graph[min_index][v] > 0:
                # graph[min_index][v] > 0 表示存在这个路径
                new_dist = dist[min_index] + graph[min_index][v]
                if dist[v] > new_dist:  # 表示值得被更新
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (dist[v], v))

    print(dist)
