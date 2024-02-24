#question link: https://www.interviewbit.com/problems/verify-prime/


class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A<=1:
            return 0
        elif A == 2:
            return 1
        elif A%2==0:
            return 0
        for i in range(3, int(A**0.5)+1):
            if A%i==0:
                return 0
        return 1
