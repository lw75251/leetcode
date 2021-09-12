"""
employees    
+---------------+---------+     
| id            | int     |
| first_name    | varchar |     
| last_name     | varchar |     
| salary        | int     |     
| department_id | int     |--+  
+---------------+---------+  |  
                             |
departments                  |
+---------------+---------+  |  
| id            | int     |<-+  
| name          | varchar |     
+---------------+---------+  

Problem: Write a SQL query to select the 2nd highest salary in the engineering department. 
If more than one person shares the highest salary, the query should select the next highest salary.
"""

with ranks as (
    select
        e.salary
        , d.name
        , dense_rank() over (
            partition by e.department_id
            order by e.salary desc) r
    from employees e
    join departments d
        on e.department_id = d.id
)

select
    salary
from ranks
where r = 2 and name='engineering'