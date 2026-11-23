class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        res= "".join(ch for ch in s1 if ch not in s2 )
        res1="".join(ch for ch in s2 if ch not in s1 )
        if res+res1=="":
            return -1
        return res+res1