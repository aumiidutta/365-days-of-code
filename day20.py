#question link: https://www.interviewbit.com/problems/functions/

#Return the factorial of the number N
def factorial(N):
    fact = 1
    while N>0:
        fact *= N
        N -= 1
    return fact
