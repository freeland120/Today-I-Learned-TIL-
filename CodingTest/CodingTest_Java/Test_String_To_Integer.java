package CodingTest;

import java.util.Scanner;

public class Test_String_To_Integer {

	public int strToInt(String str) {

		int result = Integer.parseInt(str); // Integer.parseInt()�� String�� int�� ��ȯ�� �� �ִ�. but ���ڿ� �ȿ� ���ڰ� �������� ������ �߻�!

		return result;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_String_To_Integer c = new Test_String_To_Integer();

		String str1 = input.nextLine();

		System.out.println(c.strToInt(str1));

	}

}
