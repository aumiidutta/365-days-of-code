//question link: https://www.interviewbit.com/problems/single-dimensional-arrays-in-c/


using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {    
        int n = Convert.ToInt32(Console.ReadLine());
        int[] a = new int[n];
        for(int i=0; i<n; i++){
            a[i] = Convert.ToInt32(Console.ReadLine());
        }
        
        for(int i=n-1; i>=0; i--){
            Console.WriteLine(a[i]);
        }
    }
}
