# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

# 1차원 배열 풀이
N, weight = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# dp[i] = i 무게를 담았을때의 최대 가치
dp = [0] * (weight + 1)

for item in items:
    # 중복처리를 위한 역순환 탐색
    for i in range(weight, item[0] - 1, -1):
        dp[i] = max(dp[i], dp[i - item[0]] + item[1])

print(dp[weight])


# 2차원 배열 풀이
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][w] = 앞에서 i개의 물건만 고려했을 때, 무게 한도가 w일 때 얻을 수 있는 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]

    for w in range(K + 1):
        # 현재 물건을 못 넣는 경우
        if w < weight:
            dp[i][w] = dp[i - 1][w]
        # 현재 물건을 넣을 수 있는 경우
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[N][K])
