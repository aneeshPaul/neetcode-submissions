class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams= dict()

        for s in strs:
            count= [0]*26

            for ch in s:
                count[ord(ch)-ord("a")]+=1

            key= tuple(count)

            if key in anagrams:
                anagrams[key].append(s)

            else:
                anagrams[key]= [s]

        return list(anagrams.values())
        