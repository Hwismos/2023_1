select 		e.empname, e.salary
from		employee e, department d
where		d.deptname='기획'
			and	d.deptno=e.dno
            and	e.title='과장';