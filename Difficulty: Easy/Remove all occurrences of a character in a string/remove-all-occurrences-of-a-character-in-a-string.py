class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        res=" "
        for ch in range(len(s)):
            if s[ch]==c:
                continue
            else:
                res+=s[ch]
        return res
        