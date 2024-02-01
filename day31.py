#question link: https://www.interviewbit.com/problems/numpy-arrays/

import numpy as np
def main():
    arr = [1, 3, 2, 2, 5, 3, 8, 2]

    # Convert the above array into ndarray
    arr2 = np.array(arr)
    print(type(arr2))

    # Use where to find all the indexes of 2
    x = np.where(arr2 == 2)
    print(x)

if __name__ == '__main__':
    main()
