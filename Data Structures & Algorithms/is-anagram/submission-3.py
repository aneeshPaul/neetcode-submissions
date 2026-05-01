class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def count_char(word):
            count= {}
            for char in word:
                if char in count:
                    count[char] += 1
                else:
                    count.update({char:1})
            return count

        count_s= count_char(s)
        count_t= count_char(t)

        if len(count_t) != len(count_s):
            return False

        for k,v in count_s.items():
            if k not in count_t:
                return False
            if count_t[k] != v:
                return False

        return True
            
        