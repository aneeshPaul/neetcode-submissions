class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count= {}
        freq_n= [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1

        for key,val in count.items():
            freq_n[val].append(key)


        i=0
        result= []
        for freq in freq_n[::-1]:
            if freq != []:
                result.extend(freq)
                i+=len(freq)

                if i >= k:
                    return result[:k]


        



        