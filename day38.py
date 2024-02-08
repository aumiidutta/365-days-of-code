#question link: https://www.interviewbit.com/problems/validating-email-address-using-filter/


import re
pattern= r'^[\w\-]+@[\w\.-]+\.[a-zA-Z]{2,3}$'

n = int(input())
lst = []
for _ in range(n):
    email = input()
    lst.append(email)
srtd = sorted(lst)

valid = list(filter(lambda x: re.match(pattern, x), srtd))
print(valid)
