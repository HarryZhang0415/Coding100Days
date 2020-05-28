# 解题要领

构建现在的工资表和入职表，然后做差

# 隐含题意： 

现在对应的时间是to_date = '9999-01-01', 入职则需要利用employees表的hire_date字段

# 题解：

创建sCurrent表：

select e.emp_no, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
where s.to_date = '9999-01-01'

创建sStart表：

select e.emp_no, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
where s.from_date = e.hire_date

选择员工emp_no以及最终工资-初始工资作为终表：

select sCurrent.emp_no, (sCurrent.salary - sStart.salary) as growth
from sCurrent
inner join sStart
on sCurrent.emp_no = sStart.emp_no
order by growth asd;


组合语句：
select sCurrent.emp_no, (sCurrent.salary - sStart.salary) as growth
from
(
select e.emp_no, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
where s.to_date = '9999-01-01'
) as sCurrent
inner join
(
select e.emp_no, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
where s.from_date = e.hire_date
) as sStart
on sCurrent.emp_no = sStart.emp_no
order by growth asc;
