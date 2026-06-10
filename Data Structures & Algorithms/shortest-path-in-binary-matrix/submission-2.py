from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROW = len(grid) - 1
        COL = len(grid[0]) - 1

        visited = set([(0,0)])
        queue = deque([(0, 0, 1)])

        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        while queue:
            r,c,length = queue.popleft()
            if r == ROW and c == COL:
                return length
            for dr,dc in dir:
                nr, nc = r+dr, c+dc
                if (nr,nc) in visited or min(nr,nc)<0 or nr>ROW or nc>COL or grid[nr][nc]==1:
                    pass
                else:
                    queue.append((nr,nc,length + 1))
                    visited.add((nr,nc))
            

        return -1