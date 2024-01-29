#question link: https://www.interviewbit.com/problems/dictionary/

def main():
    my_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 0
    }

    # update value for key "Sunday" to 7
    my_dict["Sunday"] = 7
    
    # adding another item with key "Default" having value 0
    my_dict["Default"] = 0

    for i in sorted(my_dict):
        print ("(\'" + i + "\',", str(my_dict[i]) + ")")

if __name__ == '__main__':
    main()
