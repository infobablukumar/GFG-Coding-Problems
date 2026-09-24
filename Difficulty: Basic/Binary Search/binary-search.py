class Solution:
    def binarySearch(self, arr, k):
        # code here
        l=0
        r=len(arr)-1
        while l<=r:
            mid = l+(r - l) // 2
            if arr[mid]==k:
                return True
            elif arr[mid]<k:
                l=mid+1
            else:
                r=mid-1
        return False