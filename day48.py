#question link: https://www.interviewbit.com/problems/sum-of-7-s-multiple/


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        first_term = ((A + 6) // 7) * 7  # smallest multiple of 7 greater than or equal to A
        last_term = (B // 7) * 7         # largest multiple of 7 less than or equal to B
        n = ((last_term - first_term) // 7) + 1  # number of terms in the series
        sum_of_terms = n * (first_term + last_term) // 2
        return sum_of_terms
