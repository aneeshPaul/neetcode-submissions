class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0]*n
        suffix_max = [0]*n

        max_val = 0
        for i in range(1,n):
            max_val = max(height[i-1], max_val)
            prefix_max[i] = max_val

        max_val = 0
        for i in range(n-2,-1,-1):
            max_val = max(height[i+1], max_val)
            suffix_max[i] = max_val

        trapped = 0
        for i in range(n):
            trapped_i = max(0, (min(prefix_max[i], suffix_max[i]) - height[i]))
            trapped+= trapped_i

        return trapped