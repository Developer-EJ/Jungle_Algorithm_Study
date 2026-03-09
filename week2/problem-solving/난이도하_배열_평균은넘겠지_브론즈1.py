# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

average_up_percents = []
for i in range(C):
    scores = [int(x) for x in input().split()]
    average = sum(scores[1:]) / scores[0]

    # 리스트 컴프레헨션을 적절히 사용하자!!
    count = sum(1 for s in scores[1:] if s > average)
    average_up_percents.append(count / scores[0])

for k in average_up_percents:
    print(f"{k*100:.3f}%")
