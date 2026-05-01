class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s=""
        for s in strs:
            encoded_s= encoded_s+str(len(s))+"#"+s

        return encoded_s

    def decode(self, s: str) -> List[str]:
        strs=[]
        
        i=0
        while i < len(s):
            j=s.find("#", i)
            l= int(s[i:j])
            strs.append(s[j+1:j+l+1])
            i= j+l+1
        return strs


