# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())
words = [input() for _ in range(N)]

dic = {}
for i in range(N):
    dic[words[i]] = words[i][::-1]

for j in dic:
    if j in dic.values():
        print(len(j), j[len(j) // 2])
        break

# 더 효율적인 방법 - set 사용
N = int(input())
words = set(input().strip() for _ in range(N))

for word in words:
    if word[::-1] in words:  # set에 접근하는건 O(1)
        print(len(word), word[len(word) // 2])
        break
