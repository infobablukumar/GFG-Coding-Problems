class Solution:
    def binarySubstring(self, s):
        #code here
        count=0
        for ch in s:
            if ch=="1":
                count+=1
        return (count*(count-1))//2