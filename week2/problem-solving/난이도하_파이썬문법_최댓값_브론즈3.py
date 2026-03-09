# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []
max = 0
max_index = 0

for i in range(9):
    nums.append(int(input()))

for i in range(1, 10):
    if nums[i - 1] > max:
        max = nums[i - 1]
        max_index = i

print(max)
print(max_index)
