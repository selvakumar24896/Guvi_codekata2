package set7_01;

/**
 *
 * @author Local user
 */
import java.util.Scanner;

public class Set7_01 {

    public static void main(String[] args) {
        Scanner val = new Scanner(System.in);
        String inp1 = val.next();
        String inp2 = val.next();
        int[] ar = new int[inp1.length()];
        if (inp1.length() == inp2.length()) {
            for (int i = 0; i < inp1.length(); i++) {
                ar[i] = ((int) inp1.charAt(i) - 96) + ((int) inp2.charAt(i) - 96);
                if (ar[i] > 26) {
                    ar[i] = ar[i] % 26;
                    if (ar[i] == 0) {
                        ar[i] = 26;
                    }
                }
            }
        } else {
            System.out.print("GIVE INPUTS WITH SAME LENGTH");
        }
        for (int i = 0; i < ar.length; i++) {
            System.out.print((char) (ar[i] + 96));
        }
    }

}
