//question link: https://www.interviewbit.com/problems/loops-java/

import java.lang.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int n = inp.nextInt();
        inp.close();
        
        for (int i= 1; i<=n; i++){
            System.out.println(i);
        }
    }
}
