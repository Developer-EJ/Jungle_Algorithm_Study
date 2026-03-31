# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = [[] for _ in range(V + 1)]

    # 양방향 그래프 생성

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
