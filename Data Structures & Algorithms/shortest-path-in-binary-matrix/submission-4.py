from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROW = len(grid) - 1
        COL = len(grid[0]) - 1

        if grid[0][0] or grid[ROW][COL] == 1:
            return -1

        visited = set([(0,0)])
        queue = deque([(0, 0)])
        length = 1
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == ROW and c == COL:
                    return length
                for dr,dc in dir:
                    nr, nc = r+dr, c+dc
                    if (nr,nc) in visited or min(nr,nc)<0 or nr>ROW or nc>COL or grid[nr][nc]==1:
                        continue
                    else:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            length+=1

        return -1