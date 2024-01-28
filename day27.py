#question link: https://www.interviewbit.com/problems/set-operations/

def main():
    # Below are the three sets 
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35]) #football
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3]) #cricket
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14]) #basketball
    
    # 'set1' contains the student who loves to play all three sports
    set1 = X.intersection(Y).intersection(Z)  
    printset(set1)
    
    # 'set2' contains the student who loves to play both Football and Cricket, but don't play Basketball
    set2 = X.intersection(Y).difference(Z)
    printset(set2)
    
    # 'set3' contains the student who loves to play Cricket, but don't loves any other sport
    set3 = Y - (X.intersection(Y).intersection(Z)) - (X.intersection(Y)) - (Y.intersection(Z))
    printset(set3)

if __name__ == '__main__':
    main()
