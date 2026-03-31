# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        length_x = len(grid[0])  # 행 길이
        length_y = len(grid)  # 열 길이
        islands_count = 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def island(x, y):
            q = deque([(x, y)])
            visited[y][x] = True

            while q:
                cur_x, cur_y = q.popleft()

                # 상하좌우
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dx, dy in directions:
                    nx = cur_x + dx
                    ny = cur_y + dy

                    # 범위 체크
                    if 0 <= nx < length_x and 0 <= ny < length_y:
                        # 1이고, 아직 방문 안 했으면 q에 추가
                        if grid[ny][nx] == "1" and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))

        # 보드 전체 탐색
        for y in range(length_y):
            for x in range(length_x):
                if grid[y][x] == "1" and not visited[y][x]:
                    island(x, y)
                    islands_count += 1
        return islands_count
