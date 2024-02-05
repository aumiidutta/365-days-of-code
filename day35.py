#question link: https://www.interviewbit.com/problems/itertools-terminating-iterators/


import itertools
import operator
def main():
    arr1 = [2, 1, 3, 4, 1]
    arr2 = [1, 2, 4]
    arr3 = [10, 3, 4, 3, 5, 6, 32, 11]
    # make a new arr4 which include all the elements in order first of arr1 then arr2 and then arr3
    arr4 = list(itertools.chain(arr1, arr2, arr3))
    print(arr4)
    # using accumulate(), store the successive muliplication of elements of arr4 in a new list arr5
    arr5 = list(itertools.accumulate(arr4, operator.mul))
    print(arr5)

if __name__ == '__main__':
    main()
