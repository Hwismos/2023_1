-- 물리적 데이터베이스 설계

-- use company;

-- show tables;

-- select * from employee;

-- 인덱스 생성
-- create index EmpIndex on employee(dno, salary);

-- 인덱스가 활용되는 질의문
-- 인덱스를 생성한 두 속성에 대한 where절
-- select *
-- from employee
-- where dno=3 and salary=4000000;

-- 아래의 질의에도 활용 가능
-- select * from employee where dno>=2 and dno<=3 and salary>=3000000 and salary <= 4000000;

-- 당연히 아래 질의에도 사용 가능
-- select * from employee where dno=2;

-- 아래 질의에서는 인덱스가 활용되지 못함
-- 단독으로 인덱스를 활용하는 질의에 쓸 수 있는 속성을 앞에 둬야 함
-- 인덱스가 정의된 두 번째 이후의 애트리뷰트만 참조하는 경우
-- select * from employee where salary>=3000000 and salary <= 4000000;