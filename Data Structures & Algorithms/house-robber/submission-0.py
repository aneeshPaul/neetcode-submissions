class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)

        def rob_from(i):
            if i<0:
                return 0
            if i == 0:
                return nums[i]

            if memo[i] != -1:
                return memo[i]

            #option 1: rob current, skip next and look for the next to next
            rob_curr = nums[i] + rob_from(i-2)

            #option 2: skip current, look next
            rob_next = rob_from(i-1)

            memo[i] = max(rob_curr, rob_next)

            return memo[i]

        return rob_from(len(nums)-1)
        