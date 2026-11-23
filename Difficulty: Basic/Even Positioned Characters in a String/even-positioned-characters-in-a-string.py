class Solution:
    def getEvenCharacters(self, s: str) -> str:
        # code here
        if len(s)==1:
            return s[0]
        res=""
        for i in range(0,len(s),2):
            res+=s[i]
        return res