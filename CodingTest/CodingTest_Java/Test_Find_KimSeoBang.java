package CodingTest;

public class Test_Find_KimSeoBang {

	public String find_kim(String[] seoul) {
		
		String result = "";
		
		String KimSeoBang = "Kim";
		
		for(int i=0; i<seoul.length; i++) {
			if(seoul[i].equals(KimSeoBang)) {
				result="�輭���� ��ġ��"+i+"�� �ֽ��ϴ�!";
				break;
				
			}
			
		}
		
		return result;
	}
	
	
	
	public static void main(String[] args) {
		
		
		Test_Find_KimSeoBang c = new Test_Find_KimSeoBang();
		
		String arr[]= {"Jane","Kim"};
		
		
		System.out.println(c.find_kim(arr));
		

	}

}
