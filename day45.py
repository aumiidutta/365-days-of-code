#question link: https://www.interviewbit.com/problems/lowest-common-multiple-lcm/


import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        hcf= math.gcd(A,B)
        lcm = A*B//hcf
        return lcm
