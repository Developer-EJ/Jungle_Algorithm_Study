# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

sorted_coins = sorted(coins, reverse=True)


def find_min(amount):
    coin_count = 0
    for coin in sorted_coins:
        if amount == 0:
            break
        # amount가 coin이랑 같을때도 처리
        if coin <= amount:
            coin_count += amount // coin
            amount %= coin

    return coin_count


print(find_min(K))
