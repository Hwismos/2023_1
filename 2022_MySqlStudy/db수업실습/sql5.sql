create view		emp_planning
as 	select		e.empname, e.title, e.salary
	from		employee e, department d
    where		e.dno=d.deptno
				and d.deptname='기획';