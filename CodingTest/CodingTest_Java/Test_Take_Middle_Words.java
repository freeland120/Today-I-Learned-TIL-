package CodingTest;

import java.util.Scanner;

public class Test_Take_Middle_Words {

	public String middle_word(String s) {
		String result = "";
        
        //¦���� Ȧ���� ���� ����� �����Ѵ�! ¦���� 2���ڰ� ������ Ȧ���� 1���ڰ� �����Բ�!
        if(s.length()%2==0) {
            result = s.substring(s.length()/2-1, s.length()/2+1);
        } else {
            result = s.substring(s.length()/2,s.length()/2+1);
        }
        
        return result;
	}
	
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Test_Take_Middle_Words c = new Test_Take_Middle_Words();

		
		String str1= "abcde";
		String str2= "qwer";
		
		
		System.out.println(c.middle_word(str1));
		System.out.println(c.middle_word(str2));
		
		
	}

}
