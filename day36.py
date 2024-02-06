#question link: https://www.interviewbit.com/problems/collections-module-i/


from collections import Counter

def main():
    n = int(input())
    lst = list(map(int, input().split()))
    dct = Counter(lst)
    m = int(input())
    count = 0

    for i in range(m):
        price, choco = map(int, input().split())
        if dct[choco]>0:
            count += price
            dct[choco] -= 1
    print(count)

if __name__ == '__main__':
    main()
