class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>m-1 or c>n-1 or grid[r][c]=="0" or (r,c) in seen:
                return
            seen.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    total+=1
                    dfs(i,j)

        return total
        