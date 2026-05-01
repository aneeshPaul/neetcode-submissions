class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        l=0
        char_map= dict()
        max_char= None

        for r in range(len(s)):
            if s[r] in char_map:
                char_map[s[r]]+=1
            else:
                char_map[s[r]]=1                

            top_freq  = max(char_map.values())
            while k < r-l+1 - top_freq:
                char_map[s[l]]-=1
                l+=1
            max_count = max(max_count, r-l+1)

        return max_count
                


        