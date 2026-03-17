# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

N = int(input())
L = list(map(int, input().split()))
L.sort()


def blend(arr, target):
    l_pointer = 0
    r_pointer = len(arr) - 1
    best_comb = 0, 0
    best_sum = float("inf")

    while l_pointer < r_pointer:
        sum = arr[l_pointer] + arr[r_pointer]

        if abs(sum) < abs(best_sum):
            best_sum = sum
            best_comb = arr[l_pointer], arr[r_pointer]

        if sum == target:
            break
        elif sum > target:
            r_pointer -= 1
        else:
            l_pointer += 1
    return best_comb


a, b = blend(L, 0)
print(a, b)
