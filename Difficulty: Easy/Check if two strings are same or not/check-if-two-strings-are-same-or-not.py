class Solution:
    def areStringsSame(self, s1, s2):
        # code here
        if len(s1)!=len(s2):
            return False
        if len(s1)==len(s2):
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    return False
        return True