#question link: https://www.interviewbit.com/problems/nested-list/

def main():
    my_list = [['a', 'b'], ['cc', 'dd', ['eee', 'fff']], ['g', 'h']]
    
    # insert a new list [1, 2, 3] at the end of my_list
    my_list.append([1, 2, 3])
    print(my_list)

    # Delete 'eee' from the list
    my_list[1][2].remove('eee')
    print(my_list)

if __name__ == '__main__':
    main()
