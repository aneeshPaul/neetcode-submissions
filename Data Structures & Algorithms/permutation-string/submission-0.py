class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        count1 = dict()
        for char in s1:
            count1[char] = 1 + count1.get(char, 0)

        while r <= len(s2):
            count2= dict()
            for char in s2[l:r]:
                count2[char] = 1 + count2.get(char, 0)
            if count1 == count2:
                return True
            l+=1
            r+=1

        return False