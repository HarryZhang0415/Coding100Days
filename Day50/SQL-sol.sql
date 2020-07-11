-- Write your MySQL query statement below
--- Q1
-- teams as t
-- matches as m


select t.team_id, t.team_name,
        sum(case when t.team_id = m.host_team and m.host_goals > m.guest_goals then 3 else 0 end) + 
        sum(case when t.team_id = m.guest_team and m.guest_goals > m.host_goals then 3 else 0 end) + 
        sum(case when t.team_id = m.host_team and m.host_goals = m.guest_goals then 1 else 0 end) + 
        sum(case when t.team_id = m.guest_team and m.guest_goals = m.host_goals then 1 else 0 end) as num_points

from Teams as t
left join matches as m
on t.team_id = m.host_team or t.team_id = m.guest_team
group by t.team_id
order by num_points desc, team_id asc;


--- Write your MySQL query statement below
-- Q2
select d.name as 'department', e1.name as 'employee', e1.salary
from employee as e1
join department as d
on e1.departmentid = d.id
where 
(
    select count(distinct e2.salary)
    from employee as e2
    where e2.salary > e1.salary
    and e1.departmentid = e2.departmentid
) < 3;
