# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque

N, M, V = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
for c in graph:
    c.sort()


# 깊이 우선
def dfs(cur, arr):
    dfs_visited[cur] = True
    arr.append(cur)

    for i in graph[cur]:
        if not dfs_visited[i]:
            dfs(i, arr)


# 너비 우선
def bfs(start, arr):
    q = deque([start])
    bfs_visited[start] = True

    while q:
        cur = q.popleft()
        arr.append(cur)

        for nxt in graph[cur]:
            if not bfs_visited[nxt]:
                bfs_visited[nxt] = True
                q.append(nxt)


dfs_arr = []
bfs_arr = []
dfs(V, dfs_arr)
bfs(V, bfs_arr)
print(*dfs_arr)
print(*bfs_arr)
