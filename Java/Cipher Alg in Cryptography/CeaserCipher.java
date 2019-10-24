import java.util.*;
public class CeaserCipher {
   
	public static StringBuffer encrypt(String msg,int key)
	{
		StringBuffer res=new StringBuffer();
		for(int i=0;i<msg.length();i++)
		{
			if(Character.isUpperCase(msg.charAt(i)))
			{
				char c=(char)(((int)msg.charAt(i)+key-65)%26+65);
				res.append(c);
			}
			else
			{
				char c=(char)(((int)msg.charAt(i)+key-97)%26+97);
				res.append(c);
			}
		}
		return res;
		
	}
	public static StringBuffer decrypt(StringBuffer msg,int key)
	{
		StringBuffer res=new StringBuffer();
		for(int i=0;i<msg.length();i++)
		{
			if(Character.isUpperCase(msg.charAt(i)))
			{
				char c=(char)(((int)msg.charAt(i)-key-65)%26+65);
				res.append(c);
			}
			else
			{
				char c=(char)(((int)msg.charAt(i)-key-97)%26+97);
				res.append(c);
			}
		}
		return res;
		
	}

	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter msg to Encrypt : ");
		String msg=s.nextLine();
		System.out.println("Enter key : ");
		int key=s.nextInt();
		System.out.println("Plain text : "+msg);
		StringBuffer emsg=new StringBuffer(encrypt(msg,key));
		System.out.println("Enncrypted msg : "+emsg);
		StringBuffer dmsg=new StringBuffer(decrypt(emsg,key));
		System.out.println("Decrypted msg : "+dmsg);
		s.close();
	}
}
