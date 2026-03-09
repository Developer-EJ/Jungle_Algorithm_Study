# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
# count, index함수 기억
# 아스키코드 변환 메서드 ord와 그 반대 메서드 chr
word = input().upper()

counts = [0] * 26

for i in word:
    counts[ord(i) - ord("A")] += 1

max_count = max(counts)
if counts.count(max_count) > 1:
    print("?")
else:
    print(chr(counts.index(max_count) + ord("A")))
