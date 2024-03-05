#question link: https://www.interviewbit.com/problems/pangram-check/


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        alll = set('abcdefghijklmnopqrstuvwxyz')
        b = set(''.join(A))
        if b == alll:
            return 1
        else:
            return 0
