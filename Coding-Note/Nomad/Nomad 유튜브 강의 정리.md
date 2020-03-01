## Nomad 유튜브 강의 정리



middleware 설치 'Morgan' morgan은 logging에 도움을 주는것(무슨 일이 어디서 일어났는지를 기록)  app.use(morgan("dev"))를 사용



helmet 이라는 것도 사용할텐데 helmet은 node.js의 보안에 도움이 되는 모듈



body parser 와 cookie parser 를 깔껀데 express의 middleware이다 (cookie와 body를 다루는걸 도와줌 )

일반적으로 생각해보자면 내가 form을 생성을하면 그건 서버에 의해서 받아져야 하는데

로그인을 하기위해 아이디와 비밀번호를 입력하면

body-parser은 body로부터 정보를 얻을 수 있게 해주는거

cookie-parser은 유저에 대한 정보를 쿠키에 저장해놓을 꺼 session을 다루기 위해서





M : data

V : how does the data look (templete)

C : function that looks for the data    (controller)



내가 주로 쓰는 원칙 divide & conquer



#2.10 MVC 패턴 part 2(11:09)

routes 폴더로 나눠 놓은 이유 redirect를 편리하게 하기 위해서!

맨 처음 메인페이지에서 login을 한사람이 logout 버튼을 눌렀을 때 home으로 redirect하고 싶어지겠지? 이 때 routes.js 폴더에 정리해놓은걸 바탕으로 쉽게 처리할 수 있음

또한, 누군가 login을 하면 user profile로 redirect 하기를 원하겠지?

전체 url 구조를 알 필요 없기 때문에 편리함



이구조에서 자유로워지기 위해서 controller를 사용할것



정리하자면...

init.js 에는 app.js에서 import 한 application이 있다.

application 관련 코드들은 app.js 파일에 담겨 있다

express를 import했고, express를 실행한 결과를 app상수로 만들었다. 그리고 middleware들을 추가를 했다.

cookieParser는 cookie를 전달받아서 사용할 수 있도록 만들어주는 미들웨어이다. 사용자 인증 같은 곳에서 쿠키를 검사할 때 사용해야 하기 때문

bodyParser은 사용자가 웹사이트로 전달하는 정보들을 검사하는 미들웨어이다. request정보에서 form이나 json 형태로 된 body를 검사한다.



아바타의 사진이나 비디오를 업로드 할 때, 제목이나 댓글 같은 정보를 전달할때 form에담아서 업로드 해야 하기 때문



helmet 미들웨어는 application이 더 안전하도록 만들어준다.

morgan 미들웨어의 역할은 application에서 발생하는 모든 일들을 loggin한다는 건데 loggin은 일이 어디에서 일어나고 있는지 확인



그리고 router 3개를 사용했고

그 중 하나는 globalRouter인데 , 이 안에는 /home , /search, /join, /login, /logout URL이 담겨 있다.



userRouter 안에는 /user/ 주소들이 있다.

주소들은 모드 routes.js에 정의해두었고 한 파일이 바뀌면 모두 적용되도록 할 수 있다.

One single source of truth(한 곳에서만  정보를 보관) 더나은 코드를 만들기 위해서!

videoRouter도 있다. 모든 router의 로직들은 모두 userController 나 videoController에 정의 돼있다.



userController와 videoController 안에는 있는 것들은 모두 함수들임!!! Join,Login,Logout,User Detail 같은 것들을 리턴하고 있다.



videoController도 마찬가지이다. 이 때까지 MVC에서 Controller 부분을 했다.



pug는 express에서 view를 다루는 방식 중 하나이다. pug는 view engine

express로 HTML을 보여줄수 있는데 res.send대신에 실제 HTML을 전달할 것이다.



views 폴더안에 템플릿 파일들을 넣을 것

layout 폴더안에 main.pug



partials라는 것을 만들었는데 이건 페이지의 일부분을 나타내기 위해서임

조직적인 목적으로 쓰기 위해서 footer.pug라는 파일을 만들었음



템플릿에 정보를 추가할 시간

컨트롤러에 있는 정보를 템플릿에 추가하는 방법

한 템플릿에만 추가하거나 전체 템플릿에 추가할 수 있다.

먼저 전체 템플릿에 추가하는 방법을 살펴보자

header 템플릿이 라우트 객체에 접근하고 싶어

이때는 미들웨어를 사용해야 한다. 미들웨어는 레이어 같은 걸로 위해서 밑으로 한단계식 내려간다.



처음에 ,view engine을 pug로 설정했어 그다음 cookie를 파싱하고 body에 담긴 정보를 파싱한다. 그다음에 helmet,morgan이 있고 그다음 컨트롤러와 라우트들이 있어

locals라는 미들웨어를 사용할껀데 이건 local변수들을 global변수로 사용할 수 있도록 만들어 주는 것이라고 생각하면 된다.



함수를 만들어주는 3가지 방법

1.

app.use((req,res,next)=>{

});



2.

app.use(function(req,res,next){

});



3.

const localsMiddleware = (req,res,next)=>{

}

app.use(localsMiddleware);





home페이지에서는 비디오가 한 칸으로 보이겠지만, 누군가의 profile페이지에서도 그 비디오를 볼 수 있어야 겠지? 

웹사이트에서 계속 반복되는 코드를 복사-붙여넣기 하지 않고 재활용하는 방법이 있는데 이방법을 mixin이라고 한다.

mixin은 웹사이트에서 자주 반복되는 html코드를 담고 있다.