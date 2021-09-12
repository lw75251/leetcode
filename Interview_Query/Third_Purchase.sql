"""
`transactions` table

column	type
id	integer
user_id	integer
created_at	datetime
product_id	integer
quantity	integer
 

Given the revenue transactions table above, write a query that finds the third purchase of every user.

Output:

column	type
user_id	integer
created_at	datetime
product_id	integer
quantity	integer
"""


with orders as (
    select
        user_id
        , created_at
        , product_id
        , quantity
        , row_number() over (
            partition by user_id 
            order by created_at
        ) as order_num
    from transactions t
)

select
    user_id
    , created_at
    , product_id
    , quantity
from orders
where order_num = 3