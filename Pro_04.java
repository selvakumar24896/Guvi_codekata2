
package pro_04;

import java.util.Scanner;

/**
 *
 * @author Local user
 */
public class Pro_04 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    Scanner val = new Scanner(System.in);
        String inp1 = val.next();
        String inp2 = val.next();
        int c1=0,c2=0;
        
        if(inp2.length()>inp1.length()){
        String temp;
        temp=inp1;
        inp1=inp2;
        inp2=temp;
    }
        int[] ar=new int[inp1.length()];
        int inp2_len=inp2.length();
        for(int i=0; i<inp1.length(); i++){
                 c1=((int)inp1.charAt(i)-96);
                 if(i<inp2_len){
                 c2=((int)inp2.charAt(i)-96);
                 }else{
                     c2=0;
                 }
                 ar[i]=Math.abs(c1-c2);
        }
         int dif=0;
        for(int i=0;i<ar.length;i++){
        dif+=ar[i];
        }
        System.out.println(dif);
    }
    
}
