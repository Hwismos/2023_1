-- drop view  emp_dno3;

create view emp_dno3 (eno, ename, title)
as 	select 	empno, empname, title
	from	employee
    where	dno=3 with check option;