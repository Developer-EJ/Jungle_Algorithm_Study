# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

N = int(input())


# Bottom-Up
def tile(num):
    if num == 1:
        return 1
    if num == 2:
        return 2

    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, num + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    return dp[num]


print(tile(N))

# Top-Down
dp = {}


def tile(num):

    if num in dp:
        return dp[num]

    if num <= 2:
        return num

    dp[num] = tile(num - 1) + tile(num - 2) % 15746
    return dp[num]


print(tile(N))
