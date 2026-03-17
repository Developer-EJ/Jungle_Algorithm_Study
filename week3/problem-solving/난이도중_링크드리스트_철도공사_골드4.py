# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309


# 링크드리스트 - 철도 공사 (백준 골드4)

# 원형 링크드 리스트 버전 - 무조건 시간 초과
# import sys

# input = sys.stdin.readline


# class Node:
#     def __init__(self, num):
#         self.num = num
#         self.next = None
#         self.prev = None


# class circle_LinkedList:
#     def __init__(self):
#         self.head = None
#         self.nodes = {}  # 역 번호 모음

#     def append(self, num):
#         new_node = Node(num)
#         self.nodes[num] = new_node

#         if self.head is None:
#             self.head = new_node
#             new_node.next = new_node
#             new_node.prev = new_node
#             return

#         tail = self.head.prev

#         tail.next = new_node
#         new_node.prev = tail

#         new_node.next = self.head
#         self.head.prev = new_node

#     def insert_and_print(self, command, i, j):
#         cur = self.nodes[i]
#         new_node = Node(j)
#         self.nodes[j] = new_node

#         if command == "BN":
#             print(cur.next.num)

#             nxt = cur.next
#             new_node.prev = cur
#             new_node.next = nxt
#             cur.next = new_node
#             nxt.prev = new_node

#         elif command == "BP":
#             print(cur.prev.num)

#             prev_node = cur.prev
#             new_node.prev = prev_node
#             new_node.next = cur
#             prev_node.next = new_node
#             cur.prev = new_node

#             if cur == self.head:
#                 self.head = new_node

#     def print_and_delete(self, command, i):
#         cur = self.nodes[i]

#         if command == "CN":
#             target = cur.next
#             print(target.num)

#             if target == cur:
#                 del self.nodes[target.num]
#                 self.head = None
#                 return

#             nxt = target.next
#             cur.next = nxt
#             nxt.prev = cur

#             if target == self.head:
#                 self.head = nxt

#             del self.nodes[target.num]

#         elif command == "CP":
#             target = cur.prev
#             print(target.num)

#             if target == cur:
#                 del self.nodes[target.num]
#                 self.head = None
#                 return

#             prev_node = target.prev
#             cur.prev = prev_node
#             prev_node.next = cur

#             if target == self.head:
#                 self.head = cur

#             del self.nodes[target.num]


# N, M = map(int, input().split())
# stations_num = list(map(int, input().split()))

# subway_map = circle_LinkedList()
# for x in stations_num:
#     subway_map.append(x)

# for _ in range(M):
#     works = input().split()
#     command = works[0]

#     match command:
#         case "BN" | "BP":
#             subway_map.insert_and_print(command, int(works[1]), int(works[2]))
#         case "CN" | "CP":
#             subway_map.print_and_delete(command, int(works[1]))

# 리스트 버전
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
stations_num = list(map(int, input().split()))

MAX = 1000001
next_station = [0] * MAX
prev_station = [0] * MAX

# 초기 원형 연결
for i in range(N):
    cur = stations_num[i]
    # 꼬리 - 헤드 관계를 잇기위해 나머지 연산
    next_station[cur] = stations_num[(i + 1) % N]
    prev_station[cur] = stations_num[(i - 1) % N]

result = []

for _ in range(M):
    works = input().split()
    command = works[0]
    i = int(works[1])

    if command == "BN":
        j = int(works[2])

        next_num = next_station[i]
        result.append(str(next_num))

        next_station[i] = j
        prev_station[j] = i
        next_station[j] = next_num
        prev_station[next_num] = j

    elif command == "BP":
        j = int(works[2])

        prev_num = prev_station[i]
        result.append(str(prev_num))

        next_station[prev_num] = j
        prev_station[j] = prev_num
        next_station[j] = i
        prev_station[i] = j

    elif command == "CN":
        target = next_station[i]
        result.append(str(target))

        next_num = next_station[target]
        next_station[i] = next_num
        prev_station[next_num] = i

    elif command == "CP":
        target = prev_station[i]
        result.append(str(target))

        prev_num = prev_station[target]
        prev_station[i] = prev_num
        next_station[prev_num] = i

print("\n".join(result))
