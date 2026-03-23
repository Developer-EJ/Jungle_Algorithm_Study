# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


def bfs(remain):
    made_cost = [False] * (k + 1)
    q = deque([0])
    made_cost[0] = True
    count_coin = 0

    while q:
        # 현재 레벨의 상태 개수
        size = len(q)

        for _ in range(size):
            cur_sum = q.popleft()

            for coin in coins:
                next_sum = cur_sum + coin

                if next_sum > remain:
                    continue

                if not made_cost[next_sum]:
                    if next_sum == remain:
                        return count_coin + 1

                    q.append(next_sum)
                    made_cost[next_sum] = True

        count_coin += 1

    return -1


print(bfs(k))
