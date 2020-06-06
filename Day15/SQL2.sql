ep table: *

select *
from employees
where not exists(
    SELECT emp_no FROM dept_emp WHERE emp_no = employees.emp_no
)