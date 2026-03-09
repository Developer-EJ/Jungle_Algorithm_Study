# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

from math import sqrt

N = int(input())
prime_count = 0

nums = [int(x) for x in input().split()]

for i in range(N):
    if nums[i] == 2:
        prime_count += 1
        continue

    if (nums[i] < 2) or (nums[i] % 2 == 0):
        continue

    sq = int(sqrt(nums[i]) + 1)
    prime_flag = False

    for j in range(3, sq, 2):
        if nums[i] % j == 0:
            prime_flag = True
            continue

    if prime_flag == False:
        prime_count += 1

print(prime_count)
