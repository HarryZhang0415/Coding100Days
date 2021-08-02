ep table: emp_no, first_name, last_name
eb table: btype
sa table: salary

1. create bonus column:
select sa.emp_no, sa.salary, eb.btype, sa.salary * eb.btype * 0.1 as bonus
from salaries as sa
INNER JOIN emp_bonus as eb
on sa.emp_no = eb.emp_no
and sa.to_date = '9999-01-01'

2. Select require rows:
select ep.emp_no, ep.first_name, ep.last_name, b.btype, b.salary, b.bonus
from employees as ep
inner JOIN (
select sa.emp_no, sa.salary, eb.btype, sa.salary * eb.btype * 0.1 as bonus
from salaries as sa
INNER JOIN emp_bonus as eb
on sa.emp_no = eb.emp_no
and sa.to_date = '9999-01-01'
) as b
on ep.emp_no = b.emp_no
/ harry often bullies Jolin
