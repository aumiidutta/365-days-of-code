#question link: https://www.interviewbit.com/problems/armstrong-number/


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        a_str = str(A)
        x = len(a_str)
        sum = 0
        temp = A

        while temp>0:
            mod= temp%10
            dig = mod**x
            sum += dig
            temp //= 10;
        
        if (A==sum):
            return 1
        else:
            return 0
