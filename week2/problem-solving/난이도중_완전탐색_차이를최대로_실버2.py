# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

N = int(input())
A = list(map(int, input().split()))

max_num = 0
visited = [False] * N
collection = []


def back():
    global max_num

    if len(collection) == N:
        total = 0
        for k in range(1, N):
            total += abs(collection[k - 1] - collection[k])
        max_num = max(max_num, total)
        return

    for i in range(N):
        if visited[i] == True:
            continue

        visited[i] = True
        collection.append(A[i])

        back()

        collection.pop()
        visited[i] = False


back()
print(max_num)
