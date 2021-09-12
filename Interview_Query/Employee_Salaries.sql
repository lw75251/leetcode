"""
Employees table
| column        | type    |
+ ------------- + ------- +
| id            | int     |
| first_name    | varchar |
| last_name     | varchar |
| salary        | int     |
| department_id | int     |
+ ------------- + ------- +

Departments table
| column          | type     |
+ --------------- + -------- +
| id              | int      |
| name            | varchar  |
+ --------------- + -------- +

download_facts table
| column          | type     |
+ --------------- + -------- +
| date            | date     |
| user_id         | int      |
| downloads       | int      |
+ --------------- + -------- +

Problem: Given the tables above, select the top 3 departments with at least
ten employees and rank them according to the percentage of their employees
making over 100K in salary.

Expected Output
| column               | type     |
+ -------------------- + -------- +
| percentage_over_100k | float    |
| department_name      | varchar  |
| number_of_employees  | int      |
+ -------------------- + -------- +
"""


with stats as (
    select
        d.name
        ,sum(case when e.salary > 100000 then 1 else 0 end) as num_over_100k
        ,count(*) as total
    from employees e
    join departments d on e.department_id = d.id
    group by 1
    having total >= 10
)

select
    num_over_100k / total as "percentage_over_100K"
    ,name as "department_name"
    ,total as "number_of_employees"
from stats
order by 1 desc
limit 3