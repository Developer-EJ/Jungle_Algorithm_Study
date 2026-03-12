# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

N = int(input())
w = [list(map(int, input().split())) for i in range(N)]
visits = [False] * N

min_path = float("inf")


def backtrack(current, index, cost):
    global min_path

    if cost > min_path:
        return

    if index == N:
        if w[current][0] != 0:
            min_path = min(min_path, cost + w[current][0])
        return

    for next in range(N):
        if visits[next] == True or w[current][next] == 0:
            continue
        visits[next] = True
        backtrack(next, index + 1, cost + w[current][next])
        visits[next] = False


visits[0] = True
backtrack(0, 1, 0)
print(min_path)
