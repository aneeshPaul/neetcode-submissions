class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_prod=[]
        prod=1

        for i in range(len(nums)):
            if i-1>=0:
                prod= prod * nums[i-1]
            prefix_prod.append(prod)
            
        suffix_prod=[]
        prod=1

        for i in range(len(nums)-1, -1, -1):
            if i+1 <= len(nums)-1:
                prod= prod * nums[i+1]
            suffix_prod.append(prod)

        suffix_prod= suffix_prod[::-1]

        res= []
        for i in range(len(nums)):
            res.append(prefix_prod[i]*suffix_prod[i])

        return res
        