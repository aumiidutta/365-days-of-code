//question link: https://www.interviewbit.com/problems/arraylist/

import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<>();
        Scanner read = new Scanner(System.in);
        while (true){
            int n= read.nextInt();
            if (n>=0){
                al.add(n);
            }
              
            else{
                break;
            }
        }

        int len = al.size();
        for (int i=len-1; i>=0; i--){
            System.out.print(al.get(i) + " ");
        } 
    }
}
