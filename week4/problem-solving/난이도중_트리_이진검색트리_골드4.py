# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# 재귀 호출 - setrecursionlimit 확장 안하면 터짐
# 매번 리스트를 만들고 비교해서, 불필요한 동작이 너무 많음
# import sys

# sys.setrecursionlimit(10**6)

# preorder = []

# for line in sys.stdin:
#     preorder.append(int(line.strip()))

# postorder = []


# def postorder_traversal(arr):
#     if not arr:
#         return

#     pivot = arr[0]

#     if len(arr) == 1:
#         postorder.append(pivot)
#         return

#     left_arr = []
#     right_arr = []

#     for i in arr:
#         if i < pivot:
#             left_arr.append(i)
#         elif i > pivot:
#             right_arr.append(i)
#         else:
#             continue

#     postorder_traversal(left_arr)
#     postorder_traversal(right_arr)
#     postorder.append(pivot)


# postorder_traversal(preorder)
# for k in postorder:
#     print(k)

# 최적화 코드
# 배열을 그때마다 만드는게 아니라, 범위만 전달한다.
# 시간은 크게 차이나지 않지만, 메모리를 훨씬 아낄 수 있다.
import sys

sys.setrecursionlimit(10**6)

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))


def postorder(start, end):
    if start > end:
        return

    root = preorder[start]
    mid = end + 1

    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)


postorder(0, len(preorder) - 1)
