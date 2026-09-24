class Solution:
    def isSorted(self, arr):
        # code here
        count=0
        for i in range(len(arr)-1):
            if arr[i]<=arr[i+1]:
                count+=1
        return count==len(arr)-1