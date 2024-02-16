#question link: https://www.interviewbit.com/problems/is-rectangle/


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if A*B == C*D or A*C == B*D or A*D == B*C:
            return 1
        else:
            return 0
