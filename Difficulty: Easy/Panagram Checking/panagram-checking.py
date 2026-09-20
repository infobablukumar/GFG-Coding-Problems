class Solution:
    def checkPangram(self, s):
        letters = set()

        for ch in s.lower():
            if 'a' <= ch <= 'z':
                letters.add(ch)

        return len(letters) == 26
        
        