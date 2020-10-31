package CodingTest;

import java.util.Scanner;

public class Test_Prime_Number {

	public int prime_number(int num) {

		int result = 0;
		boolean[] primeNumber = new boolean[num + 1];

		for (int i = 2; i <= num; i++) {
			primeNumber[i] = true; // 2~num ���� true�� �ʱ�ȭ
		}
		// ������ ���ϱ�
		int root = (int) Math.sqrt(num);

		for (int i = 2; i <= root; i++) { // 2���� num�� �����ٱ��� �˻��ϱ�
			if (primeNumber[i] = true) { // i��° ���� �Ҽ����� ���!
				for (int j = i; i * j <= num; j++) { // i ��°�� �����ϰ� �� ����� ���� false�� �ʱ�ȭ!(����� �Ҽ��� �ƴϾ�!)
					primeNumber[i * j] = false;
				}
			}
		}

		for (int i = 2; i <= num; i++) {
			if (primeNumber[i] == true) { // �Ҽ��� ���� ����
				result++;
			}

		}

		return result;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Test_Prime_Number c = new Test_Prime_Number();

		System.out.println(c.prime_number(10));
		System.out.println(c.prime_number(5));

		int a = input.nextInt();
		System.out.println(c.prime_number(a));

	}

}