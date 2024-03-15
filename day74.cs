//question link: https://www.interviewbit.com/problems/switch-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        // Use switch case to print the weekday according to the integer provided above
        // Assume 'Sunday' to be the 1st weekday
        switch(n){
            case 1:
                Console.WriteLine("Sunday");
                break;
            case 2:
                Console.WriteLine("Monday");
                break;
            case 3:
                Console.WriteLine("Tuesday");
                break;
            case 4:
                Console.WriteLine("Wednesday");
                break;
            case 5:
                Console.WriteLine("Thursday");
                break;
            case 6:
                Console.WriteLine("Friday");
                break;
            case 7:
                Console.WriteLine("Saturday");
                break;
            default:
                Console.WriteLine("");
                break;
        }
    }
}
