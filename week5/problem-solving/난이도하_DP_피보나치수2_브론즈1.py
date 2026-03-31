# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

dp1 = {}
dp2 = []


# Top-Down
def Top_Down_fibo(num):
    if num in dp1:
        return dp1[num]

    if num <= 1:
        return num

    dp1[num] = Top_Down_fibo(num - 1) + Top_Down_fibo(num - 2)
    return dp1[num]


# Bottom-Up
def Bottom_Up_fibo(num):
    dp2 = [0] * (num + 1)
    dp2[1] = 1

    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + dp2[i - 2]
    return dp2[num]


print(Top_Down_fibo(n))
print(Bottom_Up_fibo(n))
