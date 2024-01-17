create table employee (
	EMPNO		INT			NOT NULL,
    EMPNAME		CHAR(10)	UNIQUE,
    TITLE		CHAR(10)	DEFAULT	'샤원',
    MANAGER		INT,
    SALARY		int			CHECK(SALARY < 6000000),
    DNO			int			CHECK(DNO IN (1,2,3,4))		DEFAULT 1,
    primary key(empno),
    foreign key(manager) references employee(empno),
    foreign key(dno)	references	department(DEPTNO)
);