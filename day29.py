#question link: https://www.interviewbit.com/problems/classes-and-objects/


class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    stud1 = Student('Robin', 'CSE')
    stud1.printfunction()
    stud2 = Student('Rahul', 'ECE')
    stud2.printfunction()


if __name__ == '__main__':
    main()
