"""
scores table

column	type
id	integer
student	varchar
score	integer

Problem:
Given a table of students and their SAT test scores, write a query to
return the two students with the closest test scores with the score difference.
If there are multiple students with the same minimum score difference,
select the student name combination that is higher in the alphabet.

Sample Output:
one_student	other_student	score_diff
Alice	Scott	90

MAIN IDEA:
The idea here is to perform a cross join as this will create all possible
combinations between each student. Doing so will create duplication and some
unwanted rows. For example, given we have two students A and B, then a
crossjoin on itself will create AA, AB, BA, BB. We do not need to compare AA
and BB, and we can see that AB and BA are really the same thing.
If the question had asked us to return the top 5 student pairs with the closest
pairs, then we can see the difference between “!=” and “<” as both AB and BA would
have been returned with “!=” and only “AB” would be returned with “<”.

But, for the purposes of this question, we only care about the one pair,
which is why either one works technically.
"""
select
    s1.student as one_student
    , s2.student as other_student
    , abs(s1.score - s2.score) as score_diff
from scores s1
cross join scores s2
where s1.id < s2.id
order by 3,1,2
limit 1