## CatchMind 만들어보기

1.npm init

2.npm install express

3.npm install nodemon

4.npm install socket.io



src 폴더 생성

server.js 파일 만들기



script 쪽에

"start" : "nodemon --exec babel-node src/server.js" 써주기



babel은 **webpack**과 같은 **빌드시스템**과 함께 사용한다. 그러면 bable이 어떻게 동작하는지 찾아보기 쉽다.



npm install @babel-node

npm install @babel-core @babel-preset-env



.babelrc 파일 생성

{

"presets" : ["@babel/preset-env"]

}

입력

여기까지가 babel 셋팅!!!



server.js 파일에 서버 코드 작성

import express from "express";

const app = express();

const PORT = 4000;

const serverListening = ()=>{

console.log("4000 Server ready")

}



yarn start 로 실행



view templete인 pug를 쓸 차례

npm install pug



app.set("view engine","pug");





.eslintrc.js 파일생성

module.exports = {

 env: {

  browser: true,

  es6: true,

  node: true

 },

 extends: ["eslint:recommended", "plugin:prettier/recommended"],

 parserOptions: {

  ecmaVersion: 2018,

  sourceType: "module"

 },

 rules: {

  "no-console": "off"

 }

};



npm install eslint-plugin-prettier

npm install eslint-config-prettier

npm install prettier



설치후에 socketIO 가 선언이 되있는데 안쓰인다고 뜨면 성공!?



localhost://socket.io/socket.io.js



npm install morgan

import morgan from "morgan"

app.use(morgan("dev"))



io.on("connection",(socket)=>{

console.log("Somebody Connected")

});

socket 인자를 주면 Socket은 항상 서버의 이벤트를 듣고 있기 때문이다.



Socket은 request 객체이다.

express 위에서 보내는 HTTP요청 같은!

어떤 용청이나 응답을 받고 request 를 콘솔에 출력할 수 있다.

소켓은 id를 가지고 있고

let sockets=[]

매번 Socket이 연결될 때 마다 sockets라는 배열에 Socket의 id를 push할 것임





1)socket은 메모리상에 저장된다.

 2)쿠키와는 달리 서버와 클라이언트의 연결이 유지된다.

 3)서버 이벤트 on으로 발생한것을 클라이언트쪽에서 이벤트 emit나 broadcast으로 받아줘야 이벤트가 발동된다. 

4) 반대로 클라이언트에서 이벤트 on했을때 서버쪽에서 emit나 broadcast으로 받아줘야 한다.



browerify를  쓰는 이유는 구현 해야 할 게 많기 때문 require,import를 쓰기 위해서!

1.채팅하는 것

2.알림기능

3.누군가 입장하는거

4.누군가 퇴장하는거

5.각자 점수계산하기 위한 스코어 기능도 있어야 하고

6.그림 그리기 기능도 필요함

그것도 js가 필요한 작업이지 

또한, 실시간 동작이 필요하기 때문에 socketIO도 넣어줘야 한다.

그래서 엄청나게 많은 파이들이 필요함

파일 하나에 1000줄 씩 하기는 힘드니까

작은파일 여러개를 만들게 되겠지

divide and conquer 짱짱짱

gulp에서 쓰기 위해서 browerify가 만들어짐



browerify를 쓰기 위해서 babelify 같은 변환도구도 설치해줘야함