#question link: https://www.interviewbit.com/problems/product-of-all/


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mod = 10**9 + 7
        n = len(A)

        prefix_product = [1] * n
        for i in range(1, n):
            prefix_product[i] = (prefix_product[i - 1] * A[i - 1]) % mod

        suffix_product = [1] * n
        for i in range(n - 2, -1, -1):
            suffix_product[i] = (suffix_product[i + 1] * A[i + 1]) % mod

        result = [0] * n
        for i in range(n):
            result[i] = (prefix_product[i] * suffix_product[i]) % mod

        return result
