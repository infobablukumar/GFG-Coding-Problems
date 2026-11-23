class Solution:
    def valEqualToPos(self, arr):
        # code here
        j=1
        res=[]
        for i in arr:
            if i==j:
                res.append(i)
            j+=1
        return res