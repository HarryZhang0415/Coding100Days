# 题目
给出每个员工每年薪水涨幅超过5000的员工编号emp_no、薪水变更开始日期from_date以及薪水涨幅值salary_growth，并按照salary_growth逆序排列。
提示：在sqlite中获取datetime时间对应的年份函数为strftime('%Y', to_date)


CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));

# 题解：

SELECT s1.emp_no, s2.from_date, (s2.salary - s1.salary) AS salary_growth
FROM salaries AS s1, salaries AS s2
WHERE s1.emp_no=s2.emp_no
AND (STRFTIME('%Y', s2.from_date) - STRFTIME('%Y', s1.from_date) = 1
OR STRFTIME('%Y', s2.to_date) - STRFTIME('%Y', s1.to_date) = 1)
AND salary_growth>5000
ORDER BY salary_growth DESC;

题解链接：
https://www.nowcoder.com/questionTerminal/eb9b13e5257744db8265aa73de04fd44?answerType=1&f=discussion