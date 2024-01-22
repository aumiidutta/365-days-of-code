#question link: https://www.interviewbit.com/problems/string-operations/

def main():
    s = input()
    l = len(s)
    print(l) #length of the string
    
    print(s.index('a')) #index of the first occurence of 'a'
    
   s2 = s[0:l+1:2]
   print(s2) #string formed from the characters at even position

if __name__ == '__main__':
    main()
