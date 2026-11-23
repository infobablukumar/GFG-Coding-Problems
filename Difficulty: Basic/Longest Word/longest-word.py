class Solution:
    def longest(self, arr):
        # code here
        max=len(arr[0])
        j=0
        for i in range(len(arr)):
            if len(arr[i])>max:
                max=len(arr[i])
                j=i
        return arr[j]