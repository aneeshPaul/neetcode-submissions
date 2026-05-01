class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map= dict()

        for i in range(len(nums)):
            diff= target - nums[i]

            if diff in index_map:
                return [index_map[diff], i]

            index_map.update({nums[i]:i})