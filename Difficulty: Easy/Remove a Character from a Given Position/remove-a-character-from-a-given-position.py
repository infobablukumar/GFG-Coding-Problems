class Solution:
    def removeCharacter(self, s, pos):
        # code here
        if len(s)<pos:
            return s
        if pos==0:
            return s[1:]
        res=" "
        for i in range(pos):
            res+=s[i]
        for ch in range(pos+1,len(s)):
            res+=s[ch]
        return res