//question link: https://www.interviewbit.com/problems/type-conversion-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        char ch = Convert.ToChar(Console.ReadLine()); 
        int i = Convert.ToInt32(ch);
        System.Console.WriteLine(i);
    }
}
