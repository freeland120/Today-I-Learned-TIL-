## React 정리하기





### DOM이해하기 



돔이라는 것은 객체를 통하여 구조화된 문서를 표현하는 방법이며, XML or HTML로 작성된다. 웹 브라우저는 DOM을 활용하여 객체에 Javascript와 CSS를 적용한다. 

기존 DOM에는 동적 UI에 최적화 되어 있지 않다는 점이다. HTML만 봐도 정적이다라는 것을 알 수 있고 이를 Javascript나 jQquery를 사용하여 동적으로 만들어 줄수 있다. 



하지만, 페이스북이나 인스타그램과 같은 큰 규모의 웹 어플리케이션를 핸들링하기 위해서는 DOM에 직접 접근하여 변화를 주다보면, 성능상의 문제가 발생하기 시작함 => 느려진다는 것

DOM 자체는 빠르지만 DOM자체를 읽고 쓸 때의 성능은 자바스크립트 객체를 처리 할 때의 성능과 비교해서 다를게 없다. 단, 브라우저 단에서 DOM의 변화가 일어나면, 이 브라우저가 연산하고 해석하는 데 시간이 허비되는 것이다. 그래서 최소한의 DOM조작을 통하여 우리의 작업을 처리하는 방식으로 이를 개선 할 수 있다. Virtual DOM을 사용하면, 실제 DOM에 접근하여 조작하는 대신에 이를 추상화 시킨 자바스크립트 객체를 구성하여 사용합니다. 실제 DOM의 사본과 같은 역할

### React란 무엇인가?

**당신이 거기에 쓰는 모든 요소를 생성한다는 것**(자바스크립트와 함께 그것들을 만들고  그것들을 HTML로 밀어 넣는다.)



React 에서 데이터가 변하여 브라우저상의 실제 DOM을 업데이트 할 때에는 다음과 같은 3가지 절차를 밟는다. 

1.데이터가 업데이트되면, 전체 UI를 Virtual DOM에 리렌더링 한다.

2.이전 Virtual DOM에 있던 내용과 현재의 내용을 비교합니다.

3.바뀐 부분만  실제 DOM에 적용이 됩니다.

결국, 컴포넌트가 업데이트 될 때, 레이아웃 계산이 한번만 이루어지게 된다.

Virtual DOM을 쓴다고 해서 무조건 빠른게 아니다!!! 왜 가상돔을 사용하냐?

그 이유는, 지속해서 데이터가 변화하는 대규모 애플리케이션을 구축할 때 필요하다!!!

- **Virtual DOM** 을 사용합니다
- **JSX**: JSX 는 JavaScript 의 확장 문법입니다. DOM 엘리먼트들을 만들 때 JavaScript 형식으로 작성해야 하는 것을, XML 과 비슷한 형태로 작성할 수 있게 해줍니다. 이를 사용하는것은 권장사항이고 필수는 아닙니다. 하지만 사용하지 않으면 좀 불편합니다.
- **Components** React는 모두 Component 에 대한 것 입니다. React 개발을 할 때는 모든 것을 Component 로서 생각해야 합니다. 컴포넌트에 대한 자세한 내용은 앞으로 작성 될 강좌에서 다루겠습니다.



ReactJS에서는 Javascript 문법이 아닌 JSX 문법을 사용하여 UI를 템플릿화 한다!!!

필수는 아니지만 사용하면 장점이 있기 때문에 많이 사용한다.

1.JSX는 컴파일링 되면서 최적화 되므로, 빠르다

2.컴파일링 과정에서 에러를 감지 할 수 있다.

3.HTML에 익숙하다면, JSX를 사용하여 더 쉽고 빠르게 템플릿을 작성 할 수 있다.



모든 Component는 **React.Component** 를 상속합니다

**render()** 메소드에서는 컴포넌트에 렌더링 될 데이타를 정의합니다.

React JSX 는 **XML-like** Syntax 를 **native Javascript**로 변환해줍니다. 

해당 프레임워크들은 데이터단을 담당하는 모델(Model), 사용자의 화면에서 보여지게 되는 뷰(View), 그리고 사용자가 발생시키는 이벤트를 처리해주는 컨트롤러 (Controller) 로 이뤄진 MVC 패턴



Component는 HTML을 반환하는 함수이다

React를 사용하면 Component를 브라우저가 이해할 수 있는 HTML로 가져와 만들수 있다.

JSX는 javascript안의 HTML이다.

### 기억해야 할 것!

react application은 한 번에 하나의 component만 rendering 할 수 있다는 점!!!

JSX에서 두 번째로 이해해야 하는것은, Component에 정보를 보낼 수 있다는 점!!!

component에서 component로, children component로 정보를 보내는 방법을 배울것이다

ES6는 javascript의 최신버전

우리는 동적 데이터가 있는 component가 있다, 보다시피 우리는 JSX + props의 힘으로 모두 재사용 할 수 있다!



father가 children에게 data를 어떻게 보낼까? App이 어떻게 food에게 props를 사용해서 data를 보낼까? props란 이렇게 뭐든지 component에 넣게된느 것들이다. 이게 props다! props는 어디로 갈까? food의 첫 번째 argument 알겠지? 



npm install prop-types 가 하는 역할은 내가 전달받은 props가 내가 원하는 props인지를 확인해주는 것





Funtion component는 function이고 뭔가를 return한다. 그리고 screen에 표시된다.

그리고, class component는 class이다. 하지만 react component로부터 확장되고 screen에 표시된다.

react는 자동적으로 나의 class component의 render method를 자동으로 실행한다.

그렇다면 왜? class component를 가져오는 걸까? 왜냐면, class component가 가진 state라고 불리는 것 때문이다.

state는 object이다!!! 객체이기 때문에 데이터를 넣을수가 있고 이 데이터는 '변화'하는 데이터!

우리가 state를 사용하는 이유는? component의 data를 바꾸기 위해서이다!



기억해! state는 object이다. 따라서 setState()함수는 새로운 state를 받아야하고 따라서 setState({})식으로 적어 줘야한다.



#### 침대 머리맡에 두고 외워야 되는것!!!

매 순간 너가 setState를 호출할 때마다 react는 새로운 state와 함께 render function을 호출할꺼야

React는 life cycle method를 가지는데, life cycle method는 기본적으로 react  가 component를 생성하는 그리고 없애는 방법이다!



setState를 호출하면, component를 호출하고 , 먼저 render를 호출한 다음 업데이트가 완료되었다고 말하면 componentDidUpdate가 실행될 것이다.

Quiz. 처음에 우리가 render를 하면 호출된느 life cycle method는 무엇일까?  정답:componentDidMount



componentDidMount에서는 data를 fetch한다!



멤버 변수와 로컬 변수는 다르다?