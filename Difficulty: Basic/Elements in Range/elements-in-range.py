class Solution:
    def checkElements(self, start, end, arr):
        # code here
       
        present = set(arr)
        for num in range(start, end + 1):
            if num not in present:
                return False
        return True
