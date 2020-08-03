## 멀캠 Spring 숙제내용(2020.5.9)





#### 1.Spring DI(Dependency Injection) 이란 무엇인가?

![image-20200509162359900](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509162359900.png)

스프링은 객체를 생성하고 그 객체를 조립하는 데 탁월한 프레임워크 

DI를 '종속성 주입'으로 보지말고 '부품 조립'으로 봐라봐라





![image-20200509162824656](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509162824656.png)

스프링을 이해할 때 DI라는게 중요하다는데 왜 DI가 중요하냐?

![image-20200509163101170](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509163101170.png)

![image-20200509163434838](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509163434838.png)

부품을 조립하는 방법은 2가지가 있는데

1.set 함수를 이용해서 집어넣는 방법(Setter Injection)

B b = new B();

A a = new A();

a.setB(b);



2.생성자를 통해서 집어넣는 방법(Construction Injection)

B b = new B();

A a = new A(b);



우리가 컴퓨터를 산다면 조립형으로 살 수도 있고 완성형으로 살 수도 있잖아?

조립형으로 사면 내가 직접 조립함으로써 컨트롤 할 수 있지만 시간이 오래 걸린다는 단점이 있지

완성형으로 사면 컨트롤은 할 수 없지만 시간이 단축된다는 장점이 있겠지?

**이때 부품을 조립해주는 도구가 Spring이야**

어떻게 내가 부품을 조립할껀지 명시만 해주면 그걸 Spring이 해주는 역할을 한다.

DI : 부품을 조립해준다.

![image-20200509164155590](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509164155590.png)

내가 스프링에게 조립을 부탁하기전에 주문서에 어떠어떠한 회사의 제품을 쓰고 등등을 명시해줘야 한다.

우리가 쓰는 소프트웨어에서는 주문서 역할을 하는게 "XML 파일"/"Annotation"이라는 것을 통해서 명시해준다.





IoC라는게 뭐냐면~ 우리가 XML,Annotation을 통해서 주문서를 명시해주면 스프링은 주문서를 통해 객체를 생성하고 조립할 공간인 container가 필요하겠지? 그게 Ioc라고 하는 것임

"부품 컨테이너" = IoC(Inversion of Control) Container

왜 Ioc라고 부르는 걸까???



시나리오**

일단 우리가 어떤 부품을 생성해달라고 주문서에 명시를 하면 그걸 스프링은 알아듣고 부품을 생성해 컨테이너에 담는다 그다음  소부품을 생성하고 중부품을 생성하고 그 2개를 조립한다. 그리고 대부품을 생성하고 소부품,중부품,대부품을 조립한다.

![image-20200509165129402](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509165129402.png)

![image-20200509165442225](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200509165442225.png)