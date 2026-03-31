# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import math

N, M = map(int, input().split())
S = [int(input()) for _ in range(M)]

# 최대 점프 길이 제한
max_jump = int(math.sqrt(2 * N)) + 2

dp = [[float("inf")] * (max_jump + 1) for _ in range(N + 1)]

# 작은 돌은 올라가기 금지
little_stones = set(S)

if 2 not in little_stones:
    dp[2][1] = 1
else:
    print(-1)
    exit()

for i in range(2, N + 1):
    for k in range(1, max_jump + 1):
        if dp[i][k] == float("inf"):
            continue

        # 가속 점프
        if i + k + 1 <= N and (i + k + 1) not in little_stones:
            if k + 1 <= max_jump:
                dp[i + k + 1][k + 1] = min(dp[i + k + 1][k + 1], dp[i][k] + 1)

        # 일반 점프
        if i + k <= N and (i + k) not in little_stones:
            dp[i + k][k] = min(dp[i + k][k], dp[i][k] + 1)

        # 감속 점프
        if i + k - 1 <= N and k > 1 and (i + k - 1) not in little_stones:
            dp[i + k - 1][k - 1] = min(dp[i + k - 1][k - 1], dp[i][k] + 1)

result = min(dp[N])
if result == float("inf"):
    print(-1)
else:
    print(result)
