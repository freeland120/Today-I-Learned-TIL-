## 유닉스/리눅스 15강(p73~75,xinetd)



## 매우 중요한 단원!!!!(서술형 출제 할 수 있다.)

### 4)슈퍼 데몬(xinetd)





슈퍼데몬은 기존 inetd 데몬과는 다르게 **서비스별 다양한 설정 옵션을 가지고 있다.**

![image-20200417170720887](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417170720887.png)

![image-20200417171053807](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417171053807.png)

## 위 그림 시험 나왔었음 접근제어를 하기위한 속성들임

![image-20200417171936188](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417171936188.png)

cps, instances, per_source 등 접근제어를 하는 이유는 서버쪽에서 허용할 수 있는 요청의 갯수가 초과하게 된다면 서비스 접근제어를 하겠다!!!! 누군가가 악의적으로 접근하는 것을 막고 싶을꺼 아냐~





![image-20200417180048262](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417180048262.png)

 

![image-20200417180234706](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417180234706.png)

log_on_failure는 패스워드가 틀렸다라는게 아니라

"서버 자원"이 부족하거나 "접근 제어에"의한 차단을 말한다.

![image-20200417180646726](C:\Users\KAUstar\AppData\Roaming\Typora\typora-user-images\image-20200417180646726.png)