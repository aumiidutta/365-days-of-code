#question link: https://www.interviewbit.com/problems/check-palindrome/


from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        fr = Counter(A)
        lent= len(A)
        odd = sum(1 for c in fr.values() if c%2!=0)
        
        if lent%2==0:
            if odd<=1:
                return 1
            else:
                return 0
        
        else:
            if odd<=1:
                return 1
            else:
                return 0
