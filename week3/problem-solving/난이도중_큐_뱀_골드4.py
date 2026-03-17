# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

# 보드 생성
N = int(input())
board = [["X"] * N for _ in range(N)]

# 사과 생성 및 배치
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = "apple"

# 방향 변환 정보 입력
time_direction = {}
L = int(input())
for _ in range(L):
    t, d = input().split()
    time_direction[int(t)] = d

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
direction = 0

# 뱀 몸통 큐 및 머리 인덱스 생성
snake = deque()
head_x = 0
head_y = 0

# 시간
time = 0

snake.append((0, 0))
board[0][0] = "snake"
# 뱀 이동
while True:
    # 1. 다음 머리 위치 계산
    head_x = head_x + dir_x[direction]
    head_y = head_y + dir_y[direction]

    # 2. 벽 충돌 체크
    if head_x < 0 or head_y < 0 or head_x >= N or head_y >= N:
        time += 1
        break

    # 3. 몸통과 충돌 체크
    if board[head_x][head_y] == "snake":
        time += 1
        break
    # 4. 사과 유무 확인
    # 4.1 사과가 아니라면 popleft(꼬리 제거)
    if board[head_x][head_y] != "apple":
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = "X"

    # 5. 몸통 이동
    snake.append((head_x, head_y))
    board[head_x][head_y] = "snake"

    # 6. 시간 증가
    time += 1

    # 7. 방향전환 확인
    if time in time_direction:
        if time_direction[time] == "L":
            direction = (direction - 1) % 4
        elif time_direction[time] == "D":
            direction = (direction + 1) % 4


print(time)
