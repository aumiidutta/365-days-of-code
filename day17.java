//question link: https://www.interviewbit.com/problems/introduction-to-strings/

import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        String a = read.nextLine();
        String b = read.nextLine();
        read.close();
        
        System.out.println(a.length() + b.length());
        if (a.compareTo(b) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        System.out.println(a.toUpperCase() + " " + b.toUpperCase());
    }
}
