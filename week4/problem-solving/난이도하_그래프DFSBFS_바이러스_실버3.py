# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import deque

N = int(input())
M = int(input())

network = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]

for k in network:
    graph[k[0]].append(k[1])
    graph[k[1]].append(k[0])

q = deque([1])
count_connection = 0
visit = set()
visit.add(1)

while q:
    cur = q.popleft()

    for next_node in graph[cur]:
        if next_node not in visit:
            q.append(next_node)
            visit.add(next_node)
            count_connection += 1

print(count_connection)
