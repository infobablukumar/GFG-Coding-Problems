class Solution:
    def rotateArr(self, arr, d):
        # code here
        d=d%len(arr)
        l=0
        r=d-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        l=d
        r=len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        l=0
        r=len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        
        
            
        
         