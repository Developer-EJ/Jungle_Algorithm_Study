# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

# N, M = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(M)]
# graph = [[] for _ in range(N + 1)]
# visited = set()
# count_connection = 0

# # DFS 방식. 재귀가 너무 깊어지면 시관초과가 난다.
# # 노드: [갈 수 있는 노드들] 을 저장한 그래프 생성
# for k in edges:
#     graph[k[0]].append(k[1])
#     graph[k[1]].append(k[0])


# def dfs(cur):
#     visited.add(cur)

#     for j in graph[cur]:
#         if j not in visited:
#             dfs(j)


# for i in range(1, N + 1):
#     if i not in visited:
#         dfs(i)
#         count_connection += 1

# print(count_connection)

# BFS 방식
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


count_connection = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count_connection += 1

print(count_connection)
