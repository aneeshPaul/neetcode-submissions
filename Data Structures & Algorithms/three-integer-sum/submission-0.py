class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []

        nums= sorted(nums)

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l=k+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r] < -nums[k]:
                    l+=1
                elif nums[l]+nums[r] > -nums[k]:
                    r-=1
                else:
                    res.append([nums[k],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return res



        