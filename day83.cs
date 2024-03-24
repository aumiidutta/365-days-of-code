//question link: https://www.interviewbit.com/problems/classes-and-object-in-c/


/*using System;
using System.IO;
class MAIN  {
    public static void Main(string[] args) {
        int t = Convert.ToInt32(Console.ReadLine());
        for(int i=0;i<t;i++){
            string name = Console.ReadLine();
            int age = Convert.ToInt32(Console.ReadLine());
            int roll = Convert.ToInt32(Console.ReadLine());
            Student s1 = new Student();  
            s1.insert(name,age,roll);  
            s1.display(); 
         }
    }
}*/


public class Student {  
    public string name;
    public int age;
    public int roll;
    
    public void insert(string n, int a, int r) {  
        name = n;
        age = a;
        roll = r;
    }  
  
    public void display() {  
        Console.WriteLine(name + " " + age + " " + roll);
    }
}
