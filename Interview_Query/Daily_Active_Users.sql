/***
events table
| column     | type  |
| ---------- | --------- |
| id         | int       |
| user_id    | int       |
| created_at | datetime  |
| action     | string    |
| url        | string    |
| platform   | string    |
| ---------- | --------- |

Given a table of user logs with platform information
count the number of daily active users on each platform for the year of 2020.

Expected Output
| column     | type  |
| ----------= | --------- |
| platform    | string    |
| created_at  | datetime  |
| daily_users | int       |
| ----------- | --------- |
***/

select
    platform,
    created_at,
    count(distinct user_id) as daily_users
from events
where year(created_at) = 2020
group by 1,2