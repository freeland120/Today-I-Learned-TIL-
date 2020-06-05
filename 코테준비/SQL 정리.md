## SQL 정리



SELECT * FROM member;





SELECT column_name, column_name2 FROM member;



SELECT DISTINCT name FROM member;



SELECT name FROM member GROUP BY name ASC;

SELECT name FROM member GROUP BY name DESC;



SELECT * FROM member WHERE age = 34;

SELECT * FROM member WHERE phone = '010-4169-5319';



SELECT * FROM member WHERE name LIKE '박%';     //member 테이블의 이름컬럼에서 '박'씨로 시작하는 모든 값을 다 가져오겠다. 



SELECT * FROM member WHERE name LIKE '%박'; //member 테이블의 이름컬럼에서 '박'씨로 끝나는 모든 값을 다 조회하겠다.



SELECT * FROM member WHERE age >= 30;

SELECT * FROM member WHERE age >= 30 AND age <= 40;

SELECT * FROM member WHERE age between 30 AND 40;



SELECT * FROM member WHERE age <> 34;



SELECT * FROM member WHERE name in ('유덕경','유도경');



SELECT * FROM member WHERE name LIKE '박%' AND age >= 30;



SELECT * FROM member WHERE name LIKE '유%' AND (age >= 10 AND age <30);





SELECT * FROM member ORDER BY name DESC;

SELECT * FROM member ORDER BY name ASC;



SELECT * FROM member ORDER BY name, age;



INSERT INTO table_name VALUES('0','1','2');

INSERT INTO table_name (column1,column2,column3) VALUES(value1,value2,value3);

INSERT table_name SET

COLUMN1='VALUE1',

COLUMN2='VALUE2',

COLUMN3='VALUE3',

COLUMN4='VALUE4'





UPDATE table_name SET

column1 = value1,

column2 = value2,...

WHERE some_column = some_value;





UPDATE member SET

name = '유덕경',

age = 27

WHERE id = 1;



DELETE FROM member

WHERE some_column = some_value;



DELETE FROM member

WHERE id = 3;



SELECT * FROM table_name ORDER BY column_name DESC LIMIT 10;



SELECT * FROM table_name WHERE column_name LIKE pattern;

SELECT * FROM member WHERE name LIKE '유%';





SELECT test1.title, test2.comment FROM test1, test2 WHERE test1.id = test2.id;

SELECT A.title, B.comment FROM test1 as A, test2 as B WHERE A.id = B.id;





SELECT p_num FROM info INNER JOIN order ON info.p_num = order.p_num;



SELECT * FROM info

LEFT JOIN order

ON info.column1 = order.column1;



SELECT * FROM info as A

LEFT JOIN order as B

ON A.column1 = B.column1;



SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME,

IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%','O','X'); AS 중성화

FROM ANIMAL_INS

ORDER BY ANIMAL_INS.ANIMAL_ID;

SELECT EMPLOYEES.BRANCH_ID, SUM(EMPLOYEES.SALARY) as TOTAL
FROM EMPLOYEES
GROUP BY EMPLOYEES.BRANCH_ID
ORDER BY EMPLOYEES.BRANCH_ID ASC;