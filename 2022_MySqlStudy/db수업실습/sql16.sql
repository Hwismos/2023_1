select avg(salary)
from employee e, department d
where e.dno = d.deptno
group by e.dno;