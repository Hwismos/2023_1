-- use company;

-- create table r1 (
-- 	a		INT			NOT NULL,
--     primary key(a)
-- );

-- create table r2 (
-- 	a		INT			NOT NULL,
--     b		INT			NOT NULL,
--     primary key(a, b),
--     foreign key(a) references r1(a)
-- );

-- drop table r2;
-- drop table r1;

-- create table R1(
-- 	A int not null,
-- 	C int,
-- 	primary key(A)
-- );

-- create table R2(
-- 	B int not null,
-- 	A int not null,
-- 	primary key(B, A),
-- 	foreign key(A) references R1(A)
-- );

-- create table R3(
-- 	D int not null,
-- 	E int,
-- 	F int,
-- 	B int,
-- 	A int,
-- 	primary key(D),
-- 	foreign key(A) references R1(A),
-- 	foreign key(B) references R2(B)
-- );

create table R4(
	G int not null,
    A int,
    B int,
	primary key(G),
	foreign key(A) references R2(A),
	foreign key(B) references R2(B)
);

-- show tables;

-- select * from r1;