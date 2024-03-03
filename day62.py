#question link: https://www.interviewbit.com/problems/excel-column-number/


class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		ans=0
		for i in range(-1,-len(A)-1,-1):
			ans=ans+(ord(A[i])-64)*(26**(-i-1))
		return ans
