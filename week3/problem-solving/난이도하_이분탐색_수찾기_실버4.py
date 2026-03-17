# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
# 이분탐색은 정렬 후 시작!!

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


# arr에서 target을 찾는 메서드
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(1)
            return
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    print(0)


A.sort()
for i in B:
    binary_search(A, i)

# # set 풀이법
# N = int(input())
# A = set(map(int, input().split()))
# M = int(input())
# B = set(map(int, input().split()))

# for i in B:
#     print(1 if i in A else 0)
