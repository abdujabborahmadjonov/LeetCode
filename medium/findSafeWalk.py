from collections import deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # dist[i][j] = minimum total damage taken to reach (i, j)
        dist = [[float('inf')] * n for _ in range(m)]
        start_cost = grid[0][0]  # 1 if (0,0) itself is unsafe
        dist[0][0] = start_cost

        dq = deque([(0, 0)])

        while dq:
            i, j = dq.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    cost = grid[ni][nj]  # 0 or 1
                    nd = dist[i][j] + cost
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if cost == 0:
                            dq.appendleft((ni, nj))  # free move -> front
                        else:
                            dq.append((ni, nj))  # costly move -> back

        # health must stay >= 1, i.e. health - damage >= 1
        return health - dist[m - 1][n - 1] >= 1