//question link: https://www.interviewbit.com/problems/classes/

import java.lang.*;
import java.util.*;

class Pair{
    int first, second;
    Pair(){
        first = 10;
        second = 20;
    }
}

public class Main{
    public static void main(String[] args){
        Scanner read = new Scanner(System.in);
        int a = read.nextInt();
        read.nextLine();
        int b = read.nextInt();
        read.close();
                
        Pair obj  = new Pair();
        System.out.println(obj.first + obj.second);    
        System.out.println(a*obj.first);       
        System.out.println(b*obj.second);
    }
}
