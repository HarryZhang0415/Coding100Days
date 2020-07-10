-- Answer for Q1

-- Write your MySQL query statement below
select id,
        sum(case when month = "Jan" then revenue else NULL end) as Jan_Revenue,
        sum(case when month = "Feb" then revenue else NULL end) as Feb_Revenue,
        sum(case when month = "Mar" then revenue else NULL end) as Mar_Revenue,
        sum(case when month = "Apr" then revenue else NULL end) as Apr_Revenue,
        sum(case when month = "May" then revenue else NULL end) as May_Revenue,
        sum(case when month = "Jun" then revenue else NULL end) as Jun_Revenue,
        sum(case when month = "Jul" then revenue else NULL end) as Jul_Revenue,
        sum(case when month = "Aug" then revenue else NULL end) as Aug_Revenue,
        sum(case when month = "Sep" then revenue else NULL end) as Sep_Revenue,
        sum(case when month = "Oct" then revenue else NULL end) as Oct_Revenue,
        sum(case when month = "Nov" then revenue else NULL end) as Nov_Revenue,
        sum(case when month = "Dec" then revenue else NULL end) as Dec_Revenue
from department
group by id
order by id;

select t.request_at as "Day",
       ROUND(
           COUNT(CASE 
                    when t.status != 'completed' then 1
                    else NULL
                end) / count(id)
        ,2) as "Cancellation Rate"
from    trips as t
JOIN    users as client
on      t.client_id = client.users_id
and     client.banned = 'No'
JOIN    users as driver
ON      driver.users_id = t.driver_id
AND     driver.banned = 'No'
AND     t.request_at BETWEEN '2013-10-01' and '2013-10-03'
group by t.request_at;  