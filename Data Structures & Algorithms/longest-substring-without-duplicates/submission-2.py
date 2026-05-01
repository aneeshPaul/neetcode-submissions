class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_count = 1
        cur_count = 1

        i,j = 0,1

        while j < len(s):
            if s[j] in s[i:j]:
                cur_count = 1
                i+=1
                j=i+1
            else:
                cur_count+=1
                max_count=max(cur_count, max_count)
                j+=1

        return max_count
        