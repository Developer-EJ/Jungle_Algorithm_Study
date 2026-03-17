# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
# 비교하는 두 인자 타입이 같은지 꼼꼼히 확인하기!

M = int(input())
heights = list(map(int, input().split()))
stack = []
result = []

for i in range(M):
    while stack and stack[-1][0] < heights[i]:
        stack.pop()

    if stack:
        result.append(stack[-1][1])
    else:
        result.append("0")
    stack.append((heights[i], i + 1))

print(*result)
