#question link: https://www.interviewbit.com/problems/reverse-integer/


class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
        if A<0:
            num = 0-A #-(-A) = num
            num_str= str(num)
            l = len(num_str)
            rev_str = num_str[l-1::-1]
            rev = int(rev_str)
            revA = 0 - rev
            if revA < -2**31 or revA > 2**31 - 1:
                return 0
            else:
                return revA
        else:
            num_str= str(A)
            l = len(num_str)
            rev_str = num_str[l-1::-1]
            rev = int(rev_str)
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else:
                return rev
