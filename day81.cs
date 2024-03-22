//question link: https://www.interviewbit.com/problems/stringbuilder-in-c/


using System;
using System.IO;
using System.Text;
class MAIN  {
    public static void Main(string[] args) {
        // Declare a StringBuilder
        StringBuilder s = new StringBuilder();
        
        // Append "Interview"
        s.Append("Interview");
        
        // AppendLine "Bit"
        s.AppendLine("Bit");
        
        // Append "C# Course"
        s.Append("C# Course");
        
        // Print the current StringBuilder
        Console.WriteLine(s);
        
        // Replace "Interview" with "C# "
        s.Replace("Interview", "C# ");
        
        // Print the current StringBuilder
        Console.WriteLine(s);
        
        // Print the length of the StringBuilder
        Console.WriteLine(s.Length);
    }
}
