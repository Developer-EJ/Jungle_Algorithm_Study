# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

N = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(N)]
# 종료 시간이 같을때는, 시작 시간이 빠른 순으로 정렬해야 한다.
# 반례
# 2 2
# 1 2
# 2 3
sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

count = 0
start = 0

for meeting in sorted_meetings:
    # 만약 현재 미팅 시작시간이, start보다 크거나 같으면
    if meeting[0] >= start:
        count += 1
        start = meeting[1]

print(count)
