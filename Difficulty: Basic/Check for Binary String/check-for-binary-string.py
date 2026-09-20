class Solution:
    def isBinary(self, s):
        # code here
        count=0
        for ch in s : 
            if ch=="1" or ch=="0":
                count+=1
        if count==len(s):
            return True
        return False