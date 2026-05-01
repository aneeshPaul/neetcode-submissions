class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map= dict()

        for i in range(len(nums)):
            diff= target - nums[i]

            if diff in index_map:
                if i > index_map[diff]:
                    return [index_map[diff], i]

                else:
                    return [i, index_map[diff]]

            index_map.update({nums[i]:i})