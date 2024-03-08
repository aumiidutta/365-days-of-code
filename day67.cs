//question link: https://www.interviewbit.com/problems/variables-and-types-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        int i = Convert.ToInt32(Console.ReadLine());
        System.Console.WriteLine(i);
        
        long l = Convert.ToInt64(Console.ReadLine());
        System.Console.WriteLine(l);
        
        char c = Convert.ToChar(Console.ReadLine());
        System.Console.WriteLine(c);
        
        float f = Convert.ToSingle(Console.ReadLine());
        System.Console.WriteLine(f);
        
        double d = Convert.ToDouble(Console.ReadLine());
        System.Console.WriteLine(d);
    }
}
