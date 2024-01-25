#question link: https://www.interviewbit.com/problems/tuples/

def main():
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    tuple1 = tuple(("one", "two", "three"))
    list1= list(tuple1)
    list1[0] = 'number'
    tuplea= tuple(list1)
    print(tuplea)
  
    tuple2 = tuple(("1", "2", "3"))
    list2= list(tuple2)
    list2[0] = 'number'
    tupleb= tuple(list2)
    print(tupleb)

if __name__ == '__main__':
    main()
