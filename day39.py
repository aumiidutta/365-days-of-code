#question link: https://www.interviewbit.com/problems/regex/


import re
def main():
    txt = "The quick brown fox jumps over the lazy dog"
    
    # print the list of 'o' present in the string txt
    print(re.findall('o', txt))
    
    # print the index of first occurrence of 'h' in the string txt using search function
    h = re.search('h', txt)
    print(h.start())
    
    # convert the first 3 white-space character into '#' and print the changed txt
    text = re.sub('\s', '#', txt, 3)
    print(text)

if __name__ == '__main__':
    main()
