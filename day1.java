//question link: https://www.interviewbit.com/problems/stdin-and-stdout/

import java.lang.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner read= new Scanner(System.in);
        int a=read.nextInt();
        int b=read.nextInt();
        read.close();
        System.out.println(a);
        System.out.println(b);
    }
}
