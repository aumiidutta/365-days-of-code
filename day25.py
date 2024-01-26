#question link: https://www.interviewbit.com/problems/list-comprehensions/

def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = [s for s in str_list if len(s)%2!=0]
    print(my_list)

if __name__ == '__main__':
    main()
