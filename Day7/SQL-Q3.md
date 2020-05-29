# 题目
获取员工其当前的薪水比其manager当前薪水还高的相关信息，当前表示to_date='9999-01-01',
结果第一列给出员工的emp_no，
第二列给出其manager的manager_no，
第三列给出该员工当前的薪水emp_salary,
第四列给该员工对应的manager当前的薪水manager_salary
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL,
`emp_no` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));


# 题解

# 1. 选出员工的emp_no,emp_salary
select de.dept_no, de.emp_no, sa.salary as emp_salary
from dept_emp as de, salaries as sa
on de.emp_no = sa.emp_no
where de.to_date = '9999-01-01'
and sa.to_date = '9999-01-01'

# 2. 选出manager的manager_no, manager_salary
select dm.dept_no, dm.emp_no as manager_no, sa.salary as manager_salary
from dept_manager as dm, salaries as sa
on dm.emp_no = sa.emp_no
where dm.to_date = '9999-01-01'
and sa.to_date = '9999-01-01'

# 3. 合并公式并限定条件

select b1.emp_no, b2.manager_no, b1.emp_salary, b2.manager_salary
from (
select de.dept_no, de.emp_no, sa.salary as emp_salary
from dept_emp as de, salaries as sa
on de.emp_no = sa.emp_no
where de.to_date = '9999-01-01'
and sa.to_date = '9999-01-01'
) as b1
, 
(
select dm.dept_no, dm.emp_no as manager_no, sa.salary as manager_salary
from dept_manager as dm, salaries as sa
on dm.emp_no = sa.emp_no
where dm.to_date = '9999-01-01'
and sa.to_date = '9999-01-01'
) as b2
on b1.dept_no = b2.dept_no
where b1.emp_salary > b2.manager_salary