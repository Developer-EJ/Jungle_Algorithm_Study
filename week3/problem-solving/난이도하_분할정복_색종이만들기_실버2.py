# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630


def cut(x, y, size):
    global zero_count
    global one_count

    color = square[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            # 다르면 쪼개기
            if square[i][j] != color:
                half = size // 2
                cut(x, y, half)
                cut(x + half, y, half)
                cut(x, y + half, half)
                cut(x + half, y + half, half)
                return

    if color == 0:
        zero_count += 1
    else:
        one_count += 1
    return True


N = int(input())
square = [list(map(int, input().split())) for i in range(N)]

zero_count = 0
one_count = 0
cut(0, 0, N)
print(zero_count)
print(one_count)
