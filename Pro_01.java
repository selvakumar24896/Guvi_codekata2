import java.util.*;
//PRo level
public class Pro_01 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int n = inp.nextInt();
        String[] names = new String[n];
        for (int i = 0; in; i++) {
            names[i] = inp.next();

        }

        String result = ;
        for (int i = 0; inames.length - 1; i++) {
            result = check(names[i], names[i + 1]);
        }
        System.out.println(result);
    }

    public static String check(String str1, String str2) {
        String out = , temp;
        if (str1.length() {
            str2.length()
        }
        
            ){
            temp = str1;
            str1 = str2;
            str2 = temp;
        }
        for (int i = 0; istr1.length(); i++) {

            if (str1.charAt(i) == str2.charAt(i)) {
                out += str1.charAt(i);
            } else {
                break;
            }
        }
        return out;
    }
}
