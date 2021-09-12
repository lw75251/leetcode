/***
user_dimension table
| column     | type  |
| ---------- | ----- |
| user_id    | int   |
| account_id | type  |
| ---------- | ----- |

account_dimension table
| column     | type  |
| --------------- | -------- |
| account_id      | int      |
| paying_customer | boolean  |
| --------------- | -------- |

download_facts table
| column     | type  |
| --------------- | -------- |
| date            | date     |
| user_id         | int      |
| downloads       | int      |
| --------------- | -------- |

Problem: Find the average number of downloads for free vs paying customers broken out by day.
***/

select
    date,
    paying_customer,
    round(sum(downloads)/count(distinct u.user_id),2) average_downloads
from user_dimension u
join account_dimension a
    on u.account_id = a.account_id
join download_facts d
    on u.user_id = d.user_id
group by 1,2