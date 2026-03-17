# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# 백트래킹 풀이. 시간초과
# N = int(input())
# num_set = [int(input()) for _ in range(N)]
# # 현재 담긴 수 리스트
# num_arr = []
# # 집합 내에 존재하는 세수의 합의 최대값
# max_sum = 0


# def backtrack(start, current_arr):
#     global max_sum
#     # 만약 세 수를 담았고, 수들의 합이 집합 내에 있다면 최대값 갱신
#     if len(current_arr) == 3:
#         if sum(current_arr) in num_set:
#             max_sum = max(sum(current_arr), max_sum)
#         return

#     for i in range(start, len(num_set)):
#         num_arr.append(num_set[i])
#         backtrack(i + 1, current_arr)
#         num_arr.pop()


# backtrack(0, num_arr)
# print(max_sum)

# 핵심 아이디어: x+y+z=k -> x+y=k-z
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

two_sum = set()
max_sum = 0
# x+y 모든 집합을 set에 add
for i in range(N):
    for j in range(N):
        two_sum.add(nums[i] + nums[j])


# 제일 큰 k 값부터 탐색하여 k-z이 two_sum set 내에 있는지 체크
# 목표는 k를 구하는 것
def find_max_sum():
    for x in range(N - 1, -1, -1):
        for y in range(N):
            if nums[x] - nums[y] in two_sum:
                print(nums[x])
                return


find_max_sum()
