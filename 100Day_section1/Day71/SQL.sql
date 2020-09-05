-- 1517. Find Users With Valid E-Mails

-- Table: Users

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | name          | varchar |
-- | mail          | varchar |
-- +---------------+---------+
-- user_id is the primary key for this table.
-- This table contains information of the users signed up in a website. Some e-mails are invalid.
 

-- Write an SQL query to find the users who have valid emails.

-- A valid e-mail has a prefix name and a domain where: 

-- The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.' and/or dash '-'. The prefix name must start with a letter.
-- The domain is '@leetcode.com'.
-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Users
-- +---------+-----------+-------------------------+
-- | user_id | name      | mail                    |
-- +---------+-----------+-------------------------+
-- | 1       | Winston   | winston@leetcode.com    |
-- | 2       | Jonathan  | jonathanisgreat         |
-- | 3       | Annabelle | bella-@leetcode.com     |
-- | 4       | Sally     | sally.come@leetcode.com |
-- | 5       | Marwan    | quarz#2020@leetcode.com |
-- | 6       | David     | david69@gmail.com       |
-- | 7       | Shapiro   | .shapo@leetcode.com     |
-- +---------+-----------+-------------------------+

-- Result table:
-- +---------+-----------+-------------------------+
-- | user_id | name      | mail                    |
-- +---------+-----------+-------------------------+
-- | 1       | Winston   | winston@leetcode.com    |
-- | 3       | Annabelle | bella-@leetcode.com     |
-- | 4       | Sally     | sally.come@leetcode.com |
-- +---------+-----------+-------------------------+
-- The mail of user 2 doesn't have a domain.
-- The mail of user 5 has # sign which is not allowed.
-- The mail of user 6 doesn't have leetcode domain.
-- The mail of user 7 starts with a period.


-- Answer:

-- SELECT
--     user_id,
--     name,
--     mail
-- FROM Users
-- WHERE mail LIKE '[a-zA-Z]%@leetcode.com' AND LEFT(mail, LEN(mail) - 13) NOT LIKE '%[^0-9a-zA-Z_.-]%'


-- 1211. Queries Quality and Percentage

-- Table: Queries

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | query_name  | varchar |
-- | result      | varchar |
-- | position    | int     |
-- | rating      | int     |
-- +-------------+---------+
-- There is no primary key for this table, it may have duplicate rows.
-- This table contains information collected from some queries on a database.
-- The position column has a value from 1 to 500.
-- The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

-- We define query quality as:

-- The average of the ratio between query rating and its position.

-- We also define poor query percentage as:

-- The percentage of all queries with rating less than 3.

-- Write an SQL query to find each query_name, the quality and poor_query_percentage.

-- Both quality and poor_query_percentage should be rounded to 2 decimal places.

-- The query result format is in the following example:

-- Queries table:
-- +------------+-------------------+----------+--------+
-- | query_name | result            | position | rating |
-- +------------+-------------------+----------+--------+
-- | Dog        | Golden Retriever  | 1        | 5      |
-- | Dog        | German Shepherd   | 2        | 5      |
-- | Dog        | Mule              | 200      | 1      |
-- | Cat        | Shirazi           | 5        | 2      |
-- | Cat        | Siamese           | 3        | 3      |
-- | Cat        | Sphynx            | 7        | 4      |
-- +------------+-------------------+----------+--------+

-- Result table:
-- +------------+---------+-----------------------+
-- | query_name | quality | poor_query_percentage |
-- +------------+---------+-----------------------+
-- | Dog        | 2.50    | 33.33                 |
-- | Cat        | 0.66    | 33.33                 |
-- +------------+---------+-----------------------+

-- Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
-- Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

-- Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
-- Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

-- select query_name,
-- round(sum(cast(rating as float)/position)/cast(count(query_name) as float),2) as quality, 
-- round((sum(case when rating < 3 then 1.0 else 0 end)/ count(rating))*100,2) as poor_query_percentage  
-- from queries
-- group by query_name