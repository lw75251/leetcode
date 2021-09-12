"""
user_dimension table
| column     | type     |
+ ---------- + -------- +
| user_id    | int      |
| created_at | datetime |
| action     | string   |
| platform   | string   |
+ ---------- + -------- +

Problem: Write a query to determine the top 5 actions performed during the week
of Thanksgiving (11/22 - 11/28, 2020), and rank them based on number of times
performed.

Expected Output
| column     | type     |
+ ---------- + -------- +
| action     | string   |
| ranks      | int      |
+ ---------- + -------- +
"""

SELECT
    action
    , RANK() OVER(ORDER BY COUNT(*) DESC) ranks
FROM events
WHERE created_at BETWEEN '2020-11-22' AND '2020-11-28'
GROUP BY 1
LIMIT 5


----------------------------------------------------------
"""
My Failed Solution

Used Dense Rank vs Rank. Also, lenghtly when didn't really need to be.

`Rank` will skip the next available rankings in the cases of ties
`Dense_Rank` will use the next chronological ranking value

Example:
| Values | Dense Rank | Rank    |
+ ------ + ---------- + ------- +
| 100    | 1          | 1       |
| 90     | 2          | 2       |
| 90     | 2          | 2       |
| 70     | 3          | 4       |
+ ------ + ---------- + ------- +
"""

with stats as (
    select
        e.action
        , count(*) as num
    from events e
    where created_at
        between cast('2020-11-22' as date)
        and cast('2020-11-22' as date)
    group by 1
),

er as (
    select
        action,
        dense_rank() over (
            order by num desc
        ) ranks
    from stats
)

select
    action
    , ranks
from er
where ranks <= 5
