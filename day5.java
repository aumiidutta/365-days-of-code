//question link: https://www.interviewbit.com/problems/if-else/

import java.lang.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
       Scanner read  = new Scanner(System.in);
        int m = read.nextInt();
        read.close();
        
        if(m%3==0 && m%5==0) System.out.println("Good Number");
        else if(m%3==0 && m%5!=0) System.out.println("Bad Number");
        else if (m%3!=0 && m%5==0) System.out.println("Poor Number");
        else System.out.println(-1);
    }
}
