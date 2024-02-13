#question link: https://www.interviewbit.com/problems/sell-items/


import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        days = math.ceil(B/(A*5))
        return days
