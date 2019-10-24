import java.util.*;
public class VigenereCipher {
 public static void main(String args[])
 {   
	 Scanner s=new Scanner(System.in);
	 System.out.println("Enter Msg to Encrypt : ");
	 String p=s.nextLine();
	 System.out.println("Enter Key : ");
	 String k=s.nextLine();
	 StringBuffer emsg=new StringBuffer();
	 for(int i=0;i<p.length();i++)
	 {
		 char c=(char)((((int)p.charAt(i)-97)+((int)k.charAt(i)-97))%26+97);
		 emsg.append(c);
	 }
	 System.out.println("Encrypted msg : "+emsg);
	 StringBuffer dmsg=new StringBuffer();
	 for(int i=0;i<p.length();i++)
	 {   
		 char d;
		 int val=((int)emsg.charAt(i)-97)-((int)k.charAt(i)-97);
		 if(val<0) 
		 {
			  d=(char)((26+val)+97);
		 }
		 else d=(char)(val%26+97);
		 dmsg.append(d);
	 }
	 System.out.println("Decrypted msg : "+dmsg);
	 }
}
