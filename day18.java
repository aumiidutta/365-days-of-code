//question link: https://www.interviewbit.com/problems/substring/

import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        String a = read.nextLine();
        int l = read.nextInt();
        int r = read.nextInt();
        read.close();
        System.out.print(a.substring(l, r+1));
    }
}
