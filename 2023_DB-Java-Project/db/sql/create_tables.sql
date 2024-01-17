create table department(
	dno int not null,
    name char(10) default '개발부',
    floor int default 1,
    primary key (dno)
);

create table employee(
	eno int not null,
    name char(10) default '홍길동',
    position char(10) default '사원',
    salary int default 1000000,
    si char(10) default '서울특별시',
    gu char(10) default '동대문구',
    dong char(10) default '휘경동',
    dno int default 1,
    primary key (eno),
    foreign key (dno) references department(dno)
);

create table dependent(
	eno int not null, 
    name char(10) default '김철수', 
    sex char(10) default '남자',
    foreign key (eno) references employee(eno),
    primary key (eno, name)
);

create table project(
	pno int not null, 
    name char(10) default '홍길동', 
    budget int default 10000000, 
    manager int, 
    date char(20) default '2022-12-31', 
    primary key(pno), 
    foreign key(manager) references employee(eno)
);

create table supplier(
	sno int not null, 
    name char(10) default '홍길동', 
    credit int check (credit in (1,2,3,4,5)),
    primary key(sno)
);

create table part(
	partnum int not null, 
    name char(10) default 'cpu', 
    price int default 10000,
    primary key(partnum)
);

create table part_contain(
	main_part_num int not null, 
    sub_part_num int not null,
    foreign key(main_part_num) references part(partnum),
    foreign key(sub_part_num) references part(partnum),
    primary key(main_part_num, sub_part_num)
);

create table work(
	eno int not null, 
    pno int not null,
    foreign key(eno) references employee(eno),
    foreign key(pno) references project(pno),
    primary key(eno, pno)
);

create table project_location(
	pno int not null, 
    location char(20) default '서울시',
    primary key(pno)
);

create table supply(
	pno int not null, 
    sno int not null, 
    partnum int not null,  
    quantity int default 1,
    foreign key(pno) references project(pno),
    foreign key(sno) references supplier(sno),
    foreign key(partnum) references part(partnum),
    primary key(pno, sno, partnum)
);