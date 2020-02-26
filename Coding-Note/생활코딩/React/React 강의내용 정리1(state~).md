## React 강의내용 정리1(state~)



state는 props랑 같이 살펴 봐야한다.



사용자의 입장 / 구현자의 입장



state 값을 초기화 시키기 위한 코드

constructor(props){

super(props);

}

**내가 어떤 컴포넌트를 사용할 때 render함수보다 더 먼저 실행 시켜주고 싶을 때는 constructor안에 코드를 작성해준다!!!!**



상위 컴포넌트의 state 값을 하위 컴포넌트의 props 값으로 얼마든지 줄 수 있다! <Subject title={this.state.sujbect.title} 이렇게!!!



React에서는 state값이나 props값이 바뀔때 그 값를 가지고 있는 render함수가 다시 호출이 된다. 그렇다면 상위 컴퍼넌터가 가지고 있는 render함수가 호출이 됨으로 그 안에 있는 하위 컴포넌터의 render함수도 다 같이 호출이 된다.

그리고 화면이 다시 그려진다.



