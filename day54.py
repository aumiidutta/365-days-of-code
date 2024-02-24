#question link: https://www.interviewbit.com/problems/odd-even-rule/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        l = len(A)
        count = 0
        #b even - car odd
        #b odd - car even
        if B % 2 == 0:
            for i in range(l):
                if A[i] % 2 != 0:
                    count += 1
        else:
            for i in range(l):
                if A[i] % 2 == 0:
                    count += 1
        return count * C
