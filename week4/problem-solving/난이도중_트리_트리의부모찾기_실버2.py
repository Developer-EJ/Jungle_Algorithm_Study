# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import deque

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
graph = [[] for _ in range(N + 1)]
visited = set()

# 노드: [갈 수 있는 노드들] 을 저장한 그래프 생성
for k in edges:
    graph[k[0]].append(k[1])
    graph[k[1]].append(k[0])

# 부모 리스트
parents = [0] * (N + 1)

q = deque([1])
visited.add(1)

while q:
    cur = q.popleft()
    for j in graph[cur]:
        if j not in visited:
            q.append(j)
            visited.add(j)
            parents[j] = cur

for a in range(2, N + 1):
    print(parents[a])
