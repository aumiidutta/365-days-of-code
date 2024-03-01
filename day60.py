#question link: https://www.interviewbit.com/problems/length-of-last-word/


class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
		A = A.strip()
		lst = list(A.split(' '))
		l = len(lst)
		ll = len(lst[l-1])
		return ll
