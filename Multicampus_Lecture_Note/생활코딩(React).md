## 생활코딩(React)

기존 웹브라우저에는 엄청나게 많은 엘리먼트들이 들어가있는데 이걸 내가 사용하고 싶을때 너무 다뤄야할 요소들이 많아! 그렇기 때문에 쉽게 핸들링하기 위해서 리엑트라는 UI 라이브러리를 사용할 것임

어떻게? 리엑트에 컴포넌트를 사용해서!!!

컴포넌트를 사용하면 좋은 점

1.가독성이 높아진다

2.재사용성이 높아진다

3.유지보수가 높아진다



현대적인 웹 어플리케이션을 만드는 능력 함유



Coding -> Run -> Deploy



나는 어떻게 하면 강의로부터 자립할 수 있을까?를 항상 고민해야 함! 공식문서를 통해서 내가 스스로 습득할 수 있는 능력을 함유해야 함



npm이라는 것은 node.js에서 앱스토어 같은 역할을 한다고 생각하면 됨

바꿔서 말하면 안드로이드 진영에서 앱을 설치하려면 구글 앱스토어에 들어가서 다운을 받잖아?

그걸 node.js에서는 npm이 그 역할을 한다고 생각하면됨!



create-react-app을 하기 위해서는 npm이 필요함 이 npm을 설치하려면 node.js를 설치해야겠지?

1.node.js 설치하기

npm install -g create-react-app(npm을 global하게 컴퓨터에 설치하겠다라는 의미)

(공식 문서에서는 npx로 설치하라고 하지만 npm으로 진행)

npm과 npx의 차이점?

npm이 프로그램을 설치하는 프로그램이라고 한다면 npx는 create-react-app이라는 프로그램을 임시로 설치해서 딱 한번만  실행시키고 지우는 거라고 생각하면 됨! 컴퓨터의 메모리를 낭비하지 않겠지?

또 하나는 실행할때 마다 최신상태의 create-react-app을 설치하기 때문에 최신상태 유지가 간편



#### public 디렉토리

여기 안에는 index.html 파일이 들어가있음

#### src 디렉토리

 

index.js 안에있는 RecatDOM.render(<App/>,document.getElementById('root'));

에서 <App/> 이 React를 통해 만든 '사용자 정의 태그'가 컴포넌트이다!!!!



서비스 배포 할때는 쓸모없는 것들은 날려주고 가볍게 만들어 줘야함! 즉, 배포를 할때는 사용하지 않는 것들을 버리고 배포시켜줘야 함!

npm run build를 치면 build라는 폴더 안에 컴펙트하게 담아서 배포시켜줄 수 있음

npm install -g serve 는 웹서버 설치

npx serve -s build를 통해서 가벼운 서비스 배포 가능





컴포넌트를 만드는 방법

class Subject Component{

render(){

return ();

}

}

Subject라는 Component를 만들고 그 컴포넌트는 render라는 메서드를 갖는다  우리가 일반적으로 함수를 선언할때는 function이라는 키워드를 적어주지만 javascript에서는 class안에 소속되는 함수는 function을 생략해줄 수 있다.

컴포넌트를 만들때는 그 컴포넌트는 최상위 태그를 가지고 있어야 한다. 하나의 최상위 태그!

{this.props.name} 이러한 걸 통해 컴포넌트의 속성을 표현할 수 있다.

props를 사용하는 이유는 결국 동일한 출력값을 얻는게 아니라 Component가 속성이 달라지면 그에 따라서 화면에 동적으로 보여주고 싶기 때문이다.



<Subject title="WEB1.0" sub="YDG" />

<Subject title ="WEB2.0" sub= "LYS" />

{this.props.title}

{this.props.sub}



하나는 설명서를 볼줄 아는 것, 현재의 상태를 측정하고 분석하는것이 우리에게 필요하다! 

검색하고,질문하고~



chrome 확장 스토어에서 react-developer-tools 설치

혼자 코드 분석할 수 있는 도구!



하나의 파일안에 컴포넌트가 1000개 이상이 되면?

각각의 컴포넌트 별로 독립적인 파일로 만들어주면 좋다.



state는 props랑 짝꿍이다잉

사용자의 입장과 구현자의 입장을 생각해야한다. 

props는 사용자가 컴포넌트를 사용하는 입장에서 중요한 것

state는 그 props의 값에 따라서 내부에 구현에 필요한 데이터들 이라고 할 수 있다.

우리가 어떤 컴포넌트가 실행될때 render(){}라는 함수보다 더 먼저 실행이 되면서 그 컴포넌트를 초기화 시키고 싶은 코드는 constructor 안에다가 써준다.



즉, 컴포넌트 안에 constructor 함수가 있으면 초기화를 담당한다.



상위 컴포넌트에 있는 state값을 하위 컴포넌트가 사용하려면 title={this.state.subject.title} 이런식으로  하위 컴포넌트의 속성 값으로 전달해준다.

그리고 하위컴포넌트에서는 그 전달받은 값을 {this.props.title}로 표시

<div key={students[i].id}>{students[i].name}{students[i].age}</div>



내부상태를 저장하는 것을 state를 이용을 하고 자식 컴포넌트한테 전달하기 위해서 props를 사용한다.



React에서는 state값이나 props값이 바뀌면  해당되는 컴포넌트의 랜더함수가 호출되도록 약속되어있다.

e.preventDefault(); 함수는 이벤트가 발생했을때 나를 감싸고 있는 태그의 기본적인 동작방법을 막겠다라는 함수임 



리엑트에서 this는 컴포넌트 자신을 가리킨다! 그런데 예외적으로 컴포넌트 안에 function(){} 안에서는 this값이 아무것도 가지지 않는다 그래서 끝에 function(){}.bind(this) 이렇게 붙여줘야한다.