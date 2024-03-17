//question link: https://www.interviewbit.com/problems/jump-statements-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        int N = Convert.ToInt32(Console.ReadLine());
        for(int i=0; i<=N; i++){
            if(i%2!=0) Console.WriteLine(i);
            else continue;
        }
    }
}
