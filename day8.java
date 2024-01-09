//question link: https://www.interviewbit.com/problems/1d-array/

import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner read  = new Scanner(System.in);
        int n = read.nextInt();
        int[] a = new int[n];
        int i;
        for (i=0; i<n; i++){
            a[i] = read.nextInt();
        }
        read.close();
        for(i=n-1; i>=0; i--){
            System.out.println(a[i]);
        }
    }
}
