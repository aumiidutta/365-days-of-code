#question link: https://www.interviewbit.com/problems/string-validators/

def main():
    s = input()

    #checking for alphanumeric
    if any(char.isalnum() for char in s):
        print('True')
    else:
        print('False')

    # Checking for alphabetical
    if any(char.isalpha() for char in s):
        print('True')
    else:
        print('False')

    # Checking for digits
    if any(char.isdigit() for char in s):
        print('True')
    else:
        print('False')

    # Checking for lowercase
    if any(char.islower() for char in s):
        print('True')
    else:
        print('False')

    # Checking for uppercase
    if any(char.isupper() for char in s):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()
