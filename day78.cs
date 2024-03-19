//question link: https://www.interviewbit.com/problems/functions-in-c/


using System;
using System.IO;
class MAIN  {
    public static int addition (int x, int y){
        return x+y;
    }

    public static void Main(string[] args) {
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        int sum = addition(a, b);
        Console.WriteLine(sum);
    }
}
