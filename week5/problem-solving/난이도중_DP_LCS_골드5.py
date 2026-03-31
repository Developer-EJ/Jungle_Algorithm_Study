# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

A = input()
B = input()

len_A = len(A)
len_B = len(B)

dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for a in range(1, len_A + 1):
    for b in range(1, len_B + 1):
        if A[a - 1] == B[b - 1]:
            dp[a][b] = dp[a - 1][b - 1] + 1
        else:
            dp[a][b] = max(dp[a - 1][b], dp[a][b - 1])

print(dp[len_A][len_B])
