# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 재귀 DFS. visited를 두지 않으면, 같은 칸을 계속 다시 탐색해서 시간 초과
# import sys

# sys.setrecursionlimit(10**5)

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# visited = [[False] * N for _ in range(N)]

# def find(x, y):
#     if x >= N or y >= N:
#         return False

#     if visited[x][y]:
#         return False

#     if board[x][y] == -1:
#         return True

#     visited[x][y] = True
#     path = board[x][y]

#     return find(x, y + path) or find(x + path, y)

# if find(0, 0):
#     print("HaruHaru")
# else:
#     print("Hing")

# BFS
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
q = deque([(0, 0)])
visited[0][0] = True
found = False

while q:
    x, y = q.popleft()

    if board[x][y] == -1:
        found = True
        break

    path = board[x][y]

    dx, dy = x, y + path
    if dy < N and not visited[dx][dy]:
        visited[dx][dy] = True
        q.append((dx, dy))

    dx, dy = x + path, y
    if dx < N and not visited[dx][dy]:
        visited[dx][dy] = True
        q.append((dx, dy))

if found:
    print("HaruHaru")
else:
    print("Hing")
