#question link: https://www.interviewbit.com/problems/itertools-combinatoric-iterators/

from itertools import permutations
def main():
    s, x = input().split()
    k = int(x)
    lst = list(permutations(s, k))
    lst.sort()
    for ele in lst:
        res = ''.join(ele)
        print(res)

if __name__ == '__main__':
    main()
