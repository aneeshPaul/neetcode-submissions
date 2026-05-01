class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_n = min(nums)
        max_n = max(nums)

        num_map = [0]*(max_n - min_n+1)

        for n in nums:
            num_map[n-min_n]=1

        max_cons= 0
        cur_cons= 0

        for n in num_map:
            if n:
                cur_cons+=1
                max_cons= max(cur_cons, max_cons)
            else:
                cur_cons=0

        return max_cons

        