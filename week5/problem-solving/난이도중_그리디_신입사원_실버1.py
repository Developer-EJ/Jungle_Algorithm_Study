# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]

    # 서류 등수로 오름차순
    applicants.sort()

    count = 1
    min_interview = applicants[0][1]

    for i in range(1, N):
        if applicants[i][1] < min_interview:
            count += 1
            min_interview = applicants[i][1]

    print(count)
