# leetcode

Solutions to Leetcode Problems

## Learnings

### Algorithms

| Date Completed | Problem                                                                                 | Learnings                                                                                                                                                                                   | Tags                                       |
| -------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| 8/17/2021      | [1189](Python_Solutions/1189_Maximum_Number_of_Balloons.py)                             | Look at what is necessary to answer the problem to reduce the scope to be more efficient. <br /> Example: we only care about 5 letters in this problem, not all 26.                         |                                            |
| 8/17/2021      | [896](Python_Solutions/896_Monotonic_Array.py)                                          | For a Monotonic sequence, you can check for both increasing and decreasing at the same time                                                                                                 | Math                                       |
| 8/19/2021      | [896](Python_Solutions/441_Arranging_Coins.py)                                          | Remember that the series 1+2+...+(n-1)+n = (n\*(n+1))/2. Refresher to use Binary Search when possible to speed up brute force methods.                                                      | Binary Search, Math                        |
| 8/20/2021      | [141](Python_Solutions/141_Linked_List_Cycle.py)                                        | Reviewed Floyd's Cycle Detection Alg. Saw an interesting solution with one pointer where you can set a node as seen, and if you reach another node as seen, then you know there is a cycle. | Graphs, LinkedLists, Floyd Cycle Detection |
| 8/20/2021      | [1323](Python_Solutions/1323_Maximum_69_Number.py)                                      |                                                                                                                                                                                             | Greedy                                     |
| 8/20/2021      | [278](Python_Solutions/278_First_Bad_Version.py)                                        |                                                                                                                                                                                             | Binary Search                              |
| 8/21/2021      | [13](Python_Solutions/13_Roman_to_Integer.py)                                           |                                                                                                                                                                                             | Programming                                |
| 8/21/2021      | [397](Python_Solutions/397_Integer_Replacement.py)                                      | Refresher on Dynamic Programming and reminder that if there are repeated operations it can be faster to store those results.                                                                | Recursion, DP                              |
| 8/22/2021      | [1528](Python_Solutions/1528_Shuffle_String.py)                                         | Cleaner solution utilizes enumerate function                                                                                                                                                | Arrays                                     |
| 8/23/2021      | [606](Python_Solutions/606_Construct_String_from_Binary_Tree.py)                        | Refresher on BST Traversals. Practice understanding the problem output format output                                                                                                        | BST, Traversal                             |
| 8/23/2021      | [1779](Python_Solutions/1779_Find_Nearest_Point_That_Has_the_Same_X_or_Y_Coordinate.py) | Easy problem to practice writing helper functions to make code easier to read                                                                                                               | Programming                                |
| 8/23/2021      | [1346](Python_Solutions/1346_Check_If_N_and_Its_Double_Exist.py)                        | Similar to 2Sum                                                                                                                                                                             | Sets, Array, One Pass                      |
| 9/09/2021      | [704](Python_Solutions/704_Binary_Search.py)                                            | m = (low + high) // 2 may overflow. We should use m = low + (high-low) // 2 instead                                                                                                         | Binary Search                              |
| 9/09/2021      | [35](Python_Solutions/35_Search_Insert_Position.py)                                     | Think about how Binary Search exits and what you should return at the end                                                                                                                   | Binary Search                              |
| 9/10/2021      | [217](Python_Solutions/217_Contains_Duplicate.py)                                       |                                                                                                                                                                                             | Sets                                       |
| 9/11/2021      | [88](Python_Solutions/88_Merge_Sorted_Array.py)                                         | Think about a forward pointer, backward pointer, then two-pointer. In this case, backwards is best                                                                                          | Arrays                                     |
| 9/11/2021      | [1](Python_Solutions/1_Two_Sum.py)                                                      | Useful trick saving the difference                                                                                                                                                          | Arrays, Sets                               |

### SQL

| Date Completed | Problem                                                                 | Learnings |
| -------------- | ----------------------------------------------------------------------- | --------- |
| 8/19/2021      | [182](SQL_Solutions/182_Duplicate_Emails.sql)                           |           |
| 8/20/2021      | [181](SQL_Solutions/181_Employees_Earning_More_Than_Their_Managers.sql) |           |

# Interview Query

## Learnings

### SQL

| Date Completed | Problem                                                      | Learnings                                                                                                                                                                 | Difficulty |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 9/11/2021      | [Download_Facts](Interview_Query/Download_Facts.sql)         | Make sure you know what "level" we are using aggregate functions on. If the table you are performing on is on the incorrect level, don't rely on the aggregate functions. | Easy       |
| 9/11/2021      | [Daily_Active_Users](Interview_Query/Daily_Active_Users.sql) | Make sure you know what "level" we are using aggregate functions on. If the table you are performing on is on the incorrect level, don't rely on the aggregate functions. | Easy       |
| 9/12/2021      | [Popular_Actions](Interview_Query/Popular_Actions.sql)       | Learned about `RANK()` and `Dense_Rank()` Functions. Syntax is `RANK() OVER( ORDER BY {column} {asc/desc} )`                                                              | Easy       |
| 9/12/2021      | [Employee_Salaries](Interview_Query/Employee_Salaries.sql)   | Understand the filters before tackling the problem                                                                                                                        | Medium     |
