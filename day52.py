#question link: 


import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        if A < 2:
            return []

        primes = [True] * (A + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(math.sqrt(A)) + 1):
            if primes[i]:
                for j in range(i * i, A + 1, i):
                    primes[j] = False

        return [i for i in range(2, A + 1) if primes[i]]
