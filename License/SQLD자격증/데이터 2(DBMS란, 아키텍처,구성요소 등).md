## 데이터 2(DBMS란, 아키텍처,구성요소 등)



### 1.DBMS(Database Management System) 개요

기존에 통합 저장된 데이터를 중앙에서 관리하기 위한 소프트웨어라고 생각하면 된다.

DBMS가 나오기 전에는 "파일 시스템"을 사용했어

기존의 파일 시스템같은 경우는 데이터의 **중복성, 종속성**의 문제가 있었음

![image-20200823182313145](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823182313145.png)

![image-20200823182522942](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823182522942.png)

![image-20200823182546801](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823182546801.png)

![image-20200823182742952](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823182742952.png)

![image-20200823182825465](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823182825465.png)

SAM => ISAM(SAM에 index 기능이 추가됨 ) => VSAM

파일 시스템도 발전에 발전을 거듭해왔지만 중복성과,종속성의 문제를 더 효과적으로 해결하기 위해 DBMS가 나왔다.



#### DBMS 연혁

HDB(계층형, 계층구조) => 계층적이고, 상향->하향으로 Top-down방식으로 접근해서 데이터 처리

NDB(망형,네트워크 구조) => 계층형의 변형으로써 재편성시 고도의 기술이 요구됨

**RDB(관계형)** : 가장 널리 쓰이는 모델

00DB(객체지향형)



![image-20200823183347211](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823183347211.png)

![image-20200823183620514](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823183620514.png)

![image-20200823183738405](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823183738405.png)

오픈소스로서 postgresql 등의 DBMS도 많이 사용되고 있다.



![image-20200823184112541](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823184112541.png)



### 2.DBMS 아키텍처

![image-20200823184209501](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823184209501.png)

데이터를 통합 저장해서 공유하기 위해 구성한게 "데이터베이스"인데

이 데이터 베이스를 관리하기 위한 시스템 소프트웨어가 "DBMS"이다.

이 DBMS를 통해서 사용자는 다양한 어플리케이션을 통해서 데이터베이스를 활용할 수 있게 된다.

즉, **데이터베이스와 사용자간의 interface 역할을 하는게 DBMS이다.**

DBMS는 DB의 관리,분석,처리,운영에 대한 모든 기능을 제공하는 시스템 소프트웨어이다.



![image-20200823184637982](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823184637982.png)

오라클의 DBMS구조를 살펴보자

오라클DBMS는 "instance"와 "Database" 2가지로 나누어져있다.

instance는 데이터베이스의 작업을 수행하는 역할을 담당한다.

database는 작업의 대상이라고 할 수 있다.



instance는 작업을 수행하기 위해서 별도의 메모리 구조와 작업을 처리하기 위한 백그라운드 process로 이루어져 있습니다.



작업의 대상이 되는 database는 물리적인 파일들로 이루어져 있다. 이 물리적인 파일들 중에서 중요한건 데이터를 저장하기 위한 "데이터 파일", DB의 구조적인 정보를 담고있는 "컨트롤 파일" 등 다양한 물리적인 파일들로 이루어져 있다.



### 3.DBMS 구성요소

![image-20200823185457645](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823185457645.png)

SGA는 모든 프로세스가 공유해서 사용하는 SGA영역

PGA는 개별유저의 작업을 처리하기 위한 서버프로세스가 할당받는 영역인 PGA





![image-20200823185518246](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823185518246.png)



DBMS가 메모리 구조를 사용하는 이유는 당연히 Disc보다 빠르기 때문에



서버에 오라클을 구성하게되면 instance라는게 구성이 된다.

instance는 작업을 수행하기 위한 메모리 구조와 백그라운드 프로세스로 이루어진다.

이 때 구성되는 메모리 구조 중에 모든 프로세스가 공유하는 메모리 구조를 SGA라고 한다.

![image-20200823200002473](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823200002473.png)

SGA는 개별 용도에 따라서 역할이 각각 위와같이 나뉜다.

shared pool같은 경우는 우리가 SQL을 이용해서 DB를 조작하게 되는데 이때 실행된 SQL의 정보를 저장하는 영역이다.

![image-20200823200301095](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823200301095.png)

![image-20200823200417623](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823200417623.png)



<hr>

### 4.DBMS 동작방식

![image-20200823202845682](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823202845682.png)

사용자는 데이터베이스에 접근하기 위해 별도의 사용자 툴을 사용해야 하는데 3rd party application형태로 나와있는 많은 tool들이 있다.(토드,Orange,sql plus)

![image-20200823203153533](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823203153533.png)

1.DBMS는 작업을 처리하기 위해서 메모리와 백그라운드 프로세스로 이루어져 있는 인스턴스 구조를 구성합니다.

2.실제 DB는 물리적인 파일들로 이루어져 있다.

3.사용자는 DB접속 툴을 이용해 DB를 사용하게 된다.

4.사용자가 DB접속 툴을 실행하게 되면 별도로 '유저 프로세스'가 구동이 된다.

5.유저 프로세스로 DB서버쪽으로 접속요청을 수행한다.

6.DB서버는 유저가 요청한 것을 처리하기 위해서 '서버 프로세스'가 구동이 된다.

7.사용자 인증을 마치게 되면 컨넥션이 되고 

8.사용자는 SQL작업을 통해서 DB의 데이터를 접근하고 조작하는 작업을 수행하게 된다.

<hr>

### 5.DB시스템 개발

![image-20200823203934116](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823203934116.png)

![image-20200823204058960](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823204058960.png)

![image-20200823204245790](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823204245790.png)

![image-20200823204521615](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823204521615.png)

 

![image-20200823204620374](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200823204620374.png)