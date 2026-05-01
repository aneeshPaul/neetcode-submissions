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

        return count_s == count_t            
        