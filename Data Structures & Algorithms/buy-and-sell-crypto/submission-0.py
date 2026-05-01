class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro=0

        i,j = 0,0

        for j in range(len(prices)):
            max_pro = max(max_pro, prices[j] -prices[i])
            if prices[j] < prices[i]:
                i=j
            j+=1
        return max_pro
        