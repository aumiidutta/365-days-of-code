#question link: https://www.interviewbit.com/problems/product-of-digits/


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        prod = 1
        num = A
        if num == 0:
            return 0
        else:
            while num>0:
                mod = num%10
                prod *= mod
                num //= 10
            return prod
