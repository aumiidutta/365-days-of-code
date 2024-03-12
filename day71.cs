//question link: https://www.interviewbit.com/problems/if-else-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        int number = Convert.ToInt32(Console.ReadLine());
        if (number%2 == 0) Console.WriteLine("Even");
        else Console.WriteLine("Odd");     
    }
}
