#question link: https://www.interviewbit.com/problems/validating-phone-numbers/


import re
def main():
    pattern1 = r'^6[\d]{9}$'
    pattern2 = r'^7[\d]{9}$'
    pattern3 = r'^8[\d]{9}$'
    pattern4 = r'^9[\d]{9}$'

    n = int(input())
    for _ in range(n):
        num = input()
        if re.match(pattern1, num) or re.match(pattern2, num) or re.match(pattern3, num) or re.match(pattern4, num):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
