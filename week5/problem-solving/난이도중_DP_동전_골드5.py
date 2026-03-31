# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

testcase = int(input())

for _ in range(testcase):
    N = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    print(dp[amount])
