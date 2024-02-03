#question link: https://www.interviewbit.com/problems/itertools-infinite-iterators/


import itertools  
import string


def main():
    # print 1000 space separated integers starting from 1000 with common difference 500
    # There should be exactly one space after every integer
    count = 0
    for i in itertools.count(1000, 500):  
        if count == 1000:  
            break
        else:  
            print(i, end = ' ')
            count += 1
    print()

    # print all uppercase alphabets 15 times, printing from A-Z then repeating again
    # There should be exactly one space after every character
    count1 = 0
    for i in itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):  
        if count1 >= 15*26:
            break
        else:
            print(i, end = ' ')
            count1 += 1
    print()

    # print list of integers containing 1000 4's
    print(list(itertools.repeat(4,1000)))


if __name__ == '__main__':
    main()
