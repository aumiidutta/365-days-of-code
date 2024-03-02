#question link: https://www.interviewbit.com/problems/find-last-digit/


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        a = int(A[-1])
        b = int(B) % 4
        if b == 0:
            b = 4
        p = (a ** b) % 10
        return p
