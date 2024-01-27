#question link: https://www.interviewbit.com/problems/sets/


def main():
    s = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to the set
    s.update([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    
    # delete 2 and 3 from my_set
    s.discard(2)
    s.discard(3)
    
    l = list(s)
    l.sort()
    print(l)

if __name__ == '__main__':
    main()
