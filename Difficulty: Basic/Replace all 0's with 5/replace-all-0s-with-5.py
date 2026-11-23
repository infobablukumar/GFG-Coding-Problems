class Solution:
    def convertFive(self, n):
        # code here
        rep=0
        if n==0:
            return 5
        while n!=0:
            rem=n%10
            n=n//10
            if rem == 0:
                rep=rep*10+5
            else:
                rep=rep*10+rem
            
        n=rep
        rep=0
        while n!=0:
            rem=n%10
            n=n//10
            rep=rep*10+rem
        return rep