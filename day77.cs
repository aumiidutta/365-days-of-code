//question link: https://www.interviewbit.com/problems/strings-in-c/


using System;
using System.IO;
class MAIN {
    public static void Main(string[] args) {
        String str = Console.ReadLine();

        // Print the length of the string
        Console.WriteLine(str.Length);

        // Print the first index of the character 'a' in the string
        // If none present, print -1
        int ch = str.IndexOf('a');
        if(ch == -1) Console.WriteLine("-1");
        else Console.WriteLine(ch);

        // Print the number of occurrences of the character 'b' in the string
        char ch1 = 'b';
        int count = 0;
        foreach (char c in str) {
            if (c == ch1) {
                count++;
            }
        }
        Console.WriteLine(count);

        // Print the substring from the 1st index to the 4th index (inclusive)
        String str2 = str.Substring(2, 3);
        Console.WriteLine(str2);

        // Check if the string is equal to "InterviewBit"
        // Print the resulting boolean
        bool val = (str == "InterviewBit");
        Console.WriteLine(val);
    }
}
