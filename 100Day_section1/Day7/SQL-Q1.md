# 对所有员工的当前(to_date='9999-01-01')薪水按照salary进行按照1-N的排名，相同salary并列且按照emp_no升序排列
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));


# 解题思路

先构建不含有salary的rank表，再将rank表和salaries表内接，然后排序得到结果

1.构建rank表

select s1.emp_no, count(distinct s2.salary) as rank
from salaries as s1, salaries as s2
where s1.to_date = '9999-01-01'
and s2.to_date = '9999-01-01'
and s1.salary <= s2.salary
group by s1.emp_no

2.rank表和salaries表内接
select sa.emp_no, sa.salary, rank.rank
from salaries as sa
inner join rank
on sa.emp_no = rank.emp_no
and sa.to_date = '9999-01-01'
order by sa.salary desc, sa.emp_no asc

3.合并上述代码

select sa.emp_no, sa.salary, r.rank
from salaries as sa
inner join (
select s1.emp_no, count(distinct s2.salary) as rank
from salaries as s1, salaries as s2
where s1.to_date = '9999-01-01'
and s2.to_date = '9999-01-01'
and s1.salary <= s2.salary
group by s1.emp_no
) as r
on sa.emp_no = r.emp_no
and sa.to_date = '9999-01-01'
order by sa.salary desc, sa.emp_no asc


