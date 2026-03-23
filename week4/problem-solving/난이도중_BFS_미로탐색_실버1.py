# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())
# 붙어있는 숫자는 split 없이 input()만 해야함
board = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0, 1)])
visited = set()
visited.add((0, 0))

while q:
    x, y, path = q.popleft()
    # 도착하면 현재까지의 최단 경로 출력
    if (x, y) == (N - 1, M - 1):
        print(path)
        break

    # 왼쪽 체크
    if y > 0 and board[x][y - 1] == 1:
        if (x, y - 1) not in visited:
            q.append((x, y - 1, path + 1))
            visited.add((x, y - 1))

    # 오른쪽 체크
    if y < M - 1 and board[x][y + 1] == 1:
        if (x, y + 1) not in visited:
            q.append((x, y + 1, path + 1))
            visited.add((x, y + 1))

    # 위 체크
    if x > 0 and board[x - 1][y] == 1:
        if (x - 1, y) not in visited:
            q.append((x - 1, y, path + 1))
            visited.add((x - 1, y))

    # 아래 체크
    if x < N - 1 and board[x + 1][y] == 1:
        if (x + 1, y) not in visited:
            q.append((x + 1, y, path + 1))
            visited.add((x + 1, y))
