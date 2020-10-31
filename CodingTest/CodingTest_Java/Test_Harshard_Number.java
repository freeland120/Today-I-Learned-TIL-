package CodingTest;

import java.util.Scanner;

public class Test_Harshard_Number {

	public boolean harshard_number(int num) {

		int result = 0;
		int param = num;
		boolean answer = false;

		while (param / 10 != 0) {
			result += param % 10;
			param = param / 10;
		}

		result += param;

		if (num % result == 0) {
			answer = true;
		}

		System.out.printf("%d�� ��� �ڸ����� ����%d�Դϴ�. %d�� �ϻ��� ���ϱ��? ", num, result, num);

		return answer;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Test_Harshard_Number c = new Test_Harshard_Number();

		int a = input.nextInt();

		System.out.println(c.harshard_number(a));

	}

}
