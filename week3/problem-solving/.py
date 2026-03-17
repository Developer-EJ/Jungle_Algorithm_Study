word = input()
M = int(input())

left_stack = []
right_stack = []
for j in word:
    left_stack.append(j)

for i in range(M):
    command_input = input().split()
    command = command_input[0]

    match command:
        case "L":
            if left_stack:
                right_stack.insert(0, left_stack.pop())
        case "D":
            if right_stack:
                temp = right_stack[0]
                del right_stack[0]
                left_stack.append(temp)
        case "B":
            if left_stack:
                left_stack.pop()
        case "P":
            left_stack.append(command_input[1])

print("".join(left_stack + right_stack))
