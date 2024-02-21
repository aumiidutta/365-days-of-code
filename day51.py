#question link: https://www.interviewbit.com/problems/palindrome-integer/


class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        tmp = A
        rev = 0
        while tmp>0:
            mod = tmp % 10
            rev = (rev*10) + mod
            tmp //= 10
        if rev==A:
            return 1
        else:
            return 0
