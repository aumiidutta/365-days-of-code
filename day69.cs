//question link: https://www.interviewbit.com/problems/operators-in-c/


using System;
using System.IO;
class MAIN {
    public static void Main(string[] args) {
        string s = Console.ReadLine();
        int a = Convert.ToInt16(s);
        s = Console.ReadLine();
        int b = Convert.ToInt16(s);
            
        int sum, sub, mul, div; 
        sum = a+b;
        sub = a-b;
        mul = a*b;
        div = a/b;

        Console.WriteLine(sum);
        Console.WriteLine(sub);
        Console.WriteLine(mul);
        Console.WriteLine(div);
    }
}
