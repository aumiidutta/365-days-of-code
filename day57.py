#question link: https://www.interviewbit.com/problems/digital-root/


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        while A >= 10:
            A = sum(int(digit) for digit in str(A))
        return A
