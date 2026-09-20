class Solution:
    
    # Function to search for a character in the string
    def searchCharacter(self, s, ch):
        # code here
        for i in range(len(s)):
            if s[i]==ch[0]:
                return i
        return -1