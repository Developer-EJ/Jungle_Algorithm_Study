def nsum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


# 리스트 컴프리헨션
def nsum(n):
    return sum([i for i in range(n + 1)])


def nsum(n):
    return sum(list(range(1, n + 1)))
