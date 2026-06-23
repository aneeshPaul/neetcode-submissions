class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        ways = [1,2]
        i=3

        while i<=n:
            tmp = ways[1]
            ways[1] = ways[0] + ways[1]
            ways[0] = tmp
            i+=1
        
        return ways[1]

        