"""
transactions table

column	type
id	integer
user_id	integer
created_at	datetime
product_id	integer
quantity	integer
 

users table

column	type
id	integer
name	varchar
sex	varchar

Problem: Write a query to identify customers who placed more than three
transactions each in both 2019 and 2020.
"""

with stats as (
    select
        user_id
        , year(created_at)
        , count(*) as num_transactions
    from transactions t
    where year(created_at) in (2019, 2020)
    group by 1,2
)

select
    distinct u.name as customer_name
from stats s
join users u
    on s.user_id = u.id
where num_transactions > 3