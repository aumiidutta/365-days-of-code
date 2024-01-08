//question link: https://www.interviewbit.com/problems/methods/


import java.lang.*;
import java.util.*;
public class Main {
    public static int add(int x, int y){
            return x+y;
        }

    public static int multiply(int m, int n){
            return m*n;
        }

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int a = inp.nextInt();
        inp.nextLine();
        int b = inp.nextInt();
        inp.nextLine();
        inp.close();
        System.out.println(add(a,b));
        System.out.println(multiply(a,b));
    }
}
