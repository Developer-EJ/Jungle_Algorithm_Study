# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

N = int(input())


def Hanoi(index, start, end, middle):
    if index == 0:
        return
    Hanoi(index - 1, start, middle, end)
    print(start, end)
    Hanoi(index - 1, middle, end, start)


print(2**N - 1)
if N <= 20:
    Hanoi(N, 1, 3, 2)
