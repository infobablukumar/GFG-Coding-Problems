class Solution:
    def isSubset(self, a, b):
        # code here
        # count=0
        if len(a)<len(b):
            return False
        # for i in range(len(b)):
        #     for j in range(len(a)):
        #         if b[i]==a[j]:
        #             count+=1
        #             break
        # if count==len(b):
        #     return True
        # return False
        # test=set(a)
        # for i in b:
        #     if i not in test :
        #         return False
        # return True
        
        freq1={}
        freq2 = {}
        
        for i in range(len(a)):
            freq1[a[i]] =freq1.get(a[i],0)+1
        
        
        for i in range(len(b)):
            freq2[b[i]] =freq2.get(b[i],0)+1
        
        # for key,value in enumerate(freq2):
        #     if key in freq1:
        #         if freq2[key] != freq1[key]:
        #             return False
        
        for key in freq2:
            if key not in freq1:
                return False
            if key in freq1 and freq2[key] > freq1[key]:
                return False
                
        return True
    
    
    
    
