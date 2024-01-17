create view		emp_avgsal (dno, avgsal)
as	select		dno, avg(salary)
	from		employee
	group by	dno;