package set7_05;
import java.util.*;

public class Set7_05 {
    private static ArrayList inp=new ArrayList();
    
    public static void main(String[] args) {
        Scanner val=new Scanner(System.in);
        int n=val.nextInt();
        int q=val.nextInt();
        int m=val.nextInt();
        int[] out=new int[m];
      
        for( int i=0; i<n;i++){
           inp.add(val.nextInt());
        }
        for(int i=0; i<q; i++)
            getquery();
        
        for(int i=0; i<m; i++){
            out[i]=val.nextInt();
            if(out[i]>n){
                System.out.println("Invalid input give lessthan "+(n+1));
                i--;
            }
        }
        
        for(int i=0; i<m; i++)
            System.out.print(inp.get(out[i]-1)+" ");
        
    }
    
    public static void getquery(){
        Scanner val=new Scanner(System.in);
        System.out.println("option");
        int op=val.nextInt();
        System.out.println("li");
        int li=val.nextInt();
        System.out.println("ri");
        int ri=val.nextInt();
        switch(op){
            case 1:
                shift(li,ri);
                break;
            case 2:
                rev(li,ri);
                break;
        }
    }
    public static void shift(int li,int ri){
        int[] temp=new int[(ri-li)+1];
        int itr=0;
        for(int i=li-1;i<ri;i++){
            temp[itr]=(int)inp.get(i);
            itr++;
        }
        for(int i=0;i<temp.length;i++)
        itr=temp.length-1;
        for(int i=li-1;i<ri;i++){
            inp.set(i, temp[itr]);
            if(itr==temp.length-1){
                itr=0;
            }else{
            itr++;
            }
        }
    }
    
     public static void rev(int li,int ri){
         int temp=0;
         int range=0;
         int limit=((li-ri)*(-1));
         if(limit!=1)
             limit--;
         for(int i=li-1,j=ri-1;range<limit;i++,j--,range++){
             temp=(int)inp.get(i);
             inp.set(i, inp.get(j));
             inp.set(j, temp);
         }
    }
    
}
