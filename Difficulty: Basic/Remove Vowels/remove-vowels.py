class Solution:
	def removeVowels(self, s):
		# code here
		vowels=set("aeiou")
	
		       
		return  "".join(ch for ch in s if ch not in vowels)