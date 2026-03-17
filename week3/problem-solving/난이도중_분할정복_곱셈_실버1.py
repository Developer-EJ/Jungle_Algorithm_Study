# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

nums = list(map(int, input().split()))
A = nums[0]
B = nums[1]
C = nums[2]


def pow(base, exp):
    if exp <= 1:
        return base

    if exp % 2 == 1:
        odd = True
    else:
        odd = False
    exp = exp // 2

    half_result = pow(base, exp)

    if odd:
        return half_result * half_result * base % C
    else:
        return half_result * half_result % C


print(pow(A, B) % C)
