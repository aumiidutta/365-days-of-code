//question link: https://www.interviewbit.com/problems/loops-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        // Find the factorial of num1 and print it in a separate line
        int num1 = Convert.ToInt32(Console.ReadLine());
        int n = num1, fact = 1;
        while(n>0) {
            fact *= n;
            n--;
        }
        Console.WriteLine(fact);
        
        // Find the highest power of 2 that divides num2
        // and print it in a separate line
        int num2 =  Convert.ToInt32(Console.ReadLine());
        int p = 0;
        int high = 0;
        int div = (int)Math.Pow(2, p);
        while(num2%div == 0){
            high = p;
            p++;
            div = (int)Math.Pow(2, p);
        }
        Console.WriteLine(high);
    }
}
