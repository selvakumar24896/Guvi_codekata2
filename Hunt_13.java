package hunt_13;

import java.util.ArrayList;
import java.util.Scanner;

public class Hunt_13 {

    /**
     * @param args the command line arguments
     */
    private static ArrayList a1 = new ArrayList();
    private static int topind = -1;

    public static void main(String[] args) {
        Scanner val = new Scanner(System.in);

        int ch;
        String input;

        do {
            System.out.println("Enter your choice");
            System.out.println("1>Push\n2>pop\n3>display\n4>exit\n5>Check palindrome");
            ch = val.nextInt();
            switch (ch) {
                case 1:
                    System.out.println("Enter element to push");
                    input = val.next();
                    push(input);
                    break;
                case 2:
                    pop();
                    break;
                case 3:
                    System.out.println(peek());
                    break;
                case 4:
                    break;
                case 5:
                    System.out.println(check_palindrome());
                    break;
                default:
                    System.out.println("invalid choice");
            }
        } while (ch != 4);

    }

    public static void push(String element) {
        try {
            topind++;
            a1.add(topind, element);
        } catch (Exception e) {
            System.out.println("Exception occured: " + e);
        }

    }

    public static void pop() {
        if (topind != -1) {
            a1.remove(a1.size() - 1);
            topind--;
        } else {
            System.out.println("Stack is empty");
        }
    }

    public static String peek() {
        if (topind == -1) {
            return "Stack is empty";
        } else {
            String result = (String) a1.get(topind);
            return a1.toString();
        }
    }

    public static String check_palindrome() {
        if (topind == -1) {
            return "Stack is empty";
        } else {
            int temp = topind;
            int flag = 0;
            ArrayList a2 = new ArrayList();
            while (temp != -1) {
                a2.add(a1.get(temp));
                temp--;
            }
            for (int j = 0; j <= topind; j++) {
                if (a1.get(j).equals(a2.get(j))) {
                    flag = 0;
                } else {
                    flag = 1;
                }
            }
            if (flag == 1) {
                return "NO";
            } else {
                return "YES";
            }
        }
    }

}
