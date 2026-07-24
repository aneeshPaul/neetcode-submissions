class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[0]*n for k in range(m)]
        
        def bruteForce(i,j):
            if i==m or j ==n:
                return 0
            if cache[i][j]>0:
                return cache[i][j]
            if i==m-1 and j==n-1:
                return 1
            
            cache[i][j]= bruteForce(i+1,j) + bruteForce(i,j+1)

            return cache[i][j]

        count= bruteForce(0,0)

        return count