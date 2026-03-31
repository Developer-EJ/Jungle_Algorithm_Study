# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

words = input()

negative_parts = words.split("-")
result = sum(map(int, negative_parts[0].split("+")))


for part in negative_parts[1:]:
    result -= sum(map(int, part.split("+")))

print(result)
