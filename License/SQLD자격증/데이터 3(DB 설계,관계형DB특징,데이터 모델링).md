## 데이터 3(DB 설계,관계형DB특징,데이터 모델링)



### 1.정보 관리의 필요성

![image-20200823212731604](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823212731604.png)

데이터의 무결성을 유지하기 위한 설계와 시스템을 구축하는게 중요하다.

![image-20200823212832501](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823212832501.png)

![image-20200823213610946](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823213610946.png)

![image-20200823213757072](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823213757072.png)



### 2.관계형 데이터베이스 특징

![image-20200823213843962](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823213843962.png)

![image-20200823214101913](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823214101913.png)

<hr>

### 3.데이터 모델링

![image-20200823214229609](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823214229609.png)

![image-20200823214612152](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823214612152.png)



**데이터 모델이란?**

**현실 세계에 있는 복잡한 데이터를 Database에 어떻게 해서든 구조화 시켜서 집어 넣어야 할꺼 아냐? 그럼 이 때 무작정 집어넣는 것이 아니라 "모델"이라는걸 통해서 컴퓨터에 저장할 데이터의 논리적인 구조로 표현할 수 있다.**

#### 현실세계의 모델을 컴퓨터 시스템으로 옮기는 구체적인 과정을 '데이터 모델링'이라고 한다.





![image-20200823214648531](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823214648531.png)

![image-20200823214734028](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823214734028.png)

![image-20200823215300065](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823215300065.png)

![image-20200823215903569](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823215903569.png)

![](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823220011831.png)

<hr>

### 4.데이터 모델링 구성요소

관계형 데이터 모델링 3요소 : 엔티티,속성,관계

엔티티와 엔티티간에는 관계가 있다.

그 관계를 표시하면서 DB를 구축하는 것을 "관계형 데이터베이스"라고 한다.

![image-20200823220453851](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823220453851.png)

**엔티티는 물리적인 설계과정을 거치면 '테이블'이 되고 속성은 물리적인 설계과정을 거치면 'column'이 된다. 관계는 'foreign key'가 된다.**



![image-20200823220536836](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823220536836.png)

![image-20200823220621746](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823220621746.png)

![image-20200823220819792](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823220819792.png)

![image-20200823221607628](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823221607628.png)

<hr>

### 5.데이터 모델링 프로세스

데이터 모델링 프로세스에서 먼저 기업은 '업무 요구사항'파악을 하게 된다.

업무 요구사항은 현업에서 필요한 데이터를 수집하는 과정

![image-20200823221747858](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823221747858.png)

![image-20200823221905892](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823221905892.png)



전사적 아키텍처란 복잡한 기업의 모습을 다양한 측면에서 분석하고 표현하고 쉽게 이해할 수 있도록 정보체계를 구축하고  이를 활용한 아키텍처를 말한다.





![image-20200823222307754](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823222307754.png)

![image-20200823222558944](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823222558944.png)

![image-20200823222708773](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823222708773.png)