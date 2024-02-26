#question link: https://www.interviewbit.com/problems/find-duplicate-in-array/


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        s = set()
        for num in A:
            if num in s:
                return num
            else:
                s.add(num)
        return -1
