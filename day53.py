#question link: https://www.interviewbit.com/problems/leap-year/


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A % 4 == 0:
            if A % 100 == 0:
                if A % 400 == 0:
                    return 1
                else:
                    return 0
            else:
                return 1
        else:
            return 0
