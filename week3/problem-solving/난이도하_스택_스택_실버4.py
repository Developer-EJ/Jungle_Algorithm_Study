# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

N = int(input())

stack = []
result = []

for i in range(N):
    command_input = input().split()
    command = command_input[0]

    match command:
        case "push":
            value = int(command_input[1])
            stack.append(value)
        case "pop":
            if stack:
                result.append(str(stack.pop()))
            else:
                result.append("-1")
        case "size":
            result.append(str(len(stack)))
        case "empty":
            if stack:
                result.append("0")
            else:
                result.append("1")
        case "top":
            if stack:
                result.append(str(stack[-1]))
            else:
                result.append("-1")

print("\n".join(result))
