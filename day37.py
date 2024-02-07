#question link: https://www.interviewbit.com/problems/python-functionals-i/


from functools import reduce 
def main():
    # Use map to print the square of each numbers 
    ints = [4, 6, 3, 9, 2, 8, 12]
    lst = list(map(lambda x: x**2, ints))
    print(lst)   
    
    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
    def lent(name):
        l = len(name)
        if l<=7:
            return name
    lst_names= list(filter(lent, my_names))
    print(lst_names)

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    print(reduce(lambda x, y: x*y, my_numbers))
  
if __name__ == '__main__':
    main()
