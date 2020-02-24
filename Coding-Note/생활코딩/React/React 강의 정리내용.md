## React 강의 정리내용(정의,개발환경셋팅)

리엑트는 사용자 정의 태그 => 컴포넌트

컴포넌트를 작성함으로써 얻을 수 있는 장점

* 가독성
* 재사용성
* 유지보수



Coding => Run => Deploy



나는 어떻게 하면 강사로부터 독립할 수 있을까를 끊임없이 고민하자



공식문서에는 개발환경을 setting하는 방법이 나와있다.



공식문서에 나와있는 Toolchain이라는 것은 내 개발을 편리하게 도와줄수 있는 도구라고 생각하면 편함!!! 

create-react-app도 toolchain의 한 종류이다.



npm 이라는 것이 뭐냐???

nodeJS라는 기술을 이용해서 만들어진 여러가지 App들이 있는데 

그런 앱들을 명령어 환경에서 아주 손쉽게 설치할 수 있도록 도와주는 도구!

nodeJS 계의 구글 앱스토어 같은 느낌~



### React 개발 환경 셋팅

1. nodeJS 홈페이지에 들어가서 nodejs 프로그램 LTS 버전 설치
2. 설치를 하면 nodejs와 npm이 설치가 이루어짐 
3. cmd에서 'npm -v' 쳐서 버전이 나온다면 설치완료 

(다른 수업들과의 연관관계는 아래 지도를 통해서 볼 수 있습니다.  [https://seomal.org](https://www.youtube.com/redirect?redir_token=EHxujyZvZK6eR_8NdEmq_1d4j2N8MTU4MjYyODA0MUAxNTgyNTQxNjQx&event=video_description&v=nvRlr_qPfBc&q=https%3A%2F%2Fseomal.org))



4.npm install -g create-react-app  => npm에게 create-react-app을 글로벌하게 설치해줘!!! 설치하다가 권한이 없다고 나오면 sudo를 통해서 설치!

5.create-react-app -V 를 통해서 설치된 프로그램 버전 확인!

**공식문서에서는 npm이 프로그램을 설치하라는 프로그램이라면  npx라는 것은 create-react-app이라는 프로그램을 임시로 딱 한 번만 설치하고 지우는 프로그램이라고 생각하면 됨(PC 메모리의 낭비를 줄일 수 있음,다운받을 때 항상 최신상태의 버전을 설치하게 됨)**