class Solution:
    def rotate(self, arr):
        if len(arr) <= 1:
            return arr
        arr[:] = arr[-1:] + arr[:-1]
        
        
        