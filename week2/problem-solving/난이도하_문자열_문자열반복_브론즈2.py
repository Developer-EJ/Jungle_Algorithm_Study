# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

S = int(input())

results = []
for i in range(S):
    inputs = input().split()
    text = ""
    R = int(inputs[0])

    for j in inputs[1]:
        text += R * j
    results.append(text)

for k in results:
    print(k)
