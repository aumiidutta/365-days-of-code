#question link: https://www.interviewbit.com/problems/palindrome-string/


import re
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        ori = re.sub(r'[^a-zA-Z0-9]', '', A).lower()
        rev = ori[::-1]
        if ori == rev:
            return 1
        else:
            return 0
