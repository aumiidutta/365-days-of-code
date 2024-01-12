//question link: https://www.interviewbit.com/problems/stacks/

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        int t = read.nextInt(); //test case
        read.nextLine(); // consume the newline character

        for (int a = 0; a < t; a++) {
            String str = read.nextLine();
            int len = str.length();
            Stack<Character> stack = new Stack<>();

            boolean isBalanced = true;

            for (int i = 0; i < len; i++) {
                char currentChar = str.charAt(i);

                if (currentChar == '(') {
                    stack.push(currentChar);
                } else if (currentChar == ')') {
                    if (stack.isEmpty() || stack.pop() != '(') {
                        isBalanced = false;
                        break;
                    }
                }
            }

            if (isBalanced && stack.isEmpty()) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
