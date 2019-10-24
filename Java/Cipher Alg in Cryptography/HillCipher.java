import java.io.*;
import java.util.*;
public class HillCipher {
  public static void main(String args[])
  {
	int key[][]= {{17,17,5},{21,18,21},{2,2,19}};
	int p[]=new int[100];
	int c[]=new int[100];
	Scanner s=new Scanner(System.in);
	System.out.println("Enter plain text : ");
	String str=s.nextLine();
	for(int i=0;i<str.length();i++)
	{
		p[i]=(int)(str.charAt(i)-97);
	}
	int i=0,z=0;
	for(int a=0;a<str.length()/3;a++)
	{
		for(int j=0;j<3;j++)
		{
			for(int x=0;x<3;x++)
			{
				c[i]+=key[j][x]*p[x+z];
			}
			i++;
		}
		z+=3;
	}
	for(int itr=0;itr<str.length();itr++)
	{
		System.out.print((char)((c[itr]%26)+97));
	}
	  
  }
}
