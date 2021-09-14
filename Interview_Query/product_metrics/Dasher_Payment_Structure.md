# Problem

Let's say you work for a food delivery company. We have a payment structure for delivery drivers where they make 5% of every order. A product manager wants to launch a new payment structure for delivery drivers where delivery drivers make 2.5% of each order and $50 after each fifth order.

How would you determine the success of this new structure?

## Answer

We determine the success of this new structure by analyzing the
total payout to the delivery drivers in Scenario 1 vs Scenario 2.

Scenario 1
Let there be 10 orders, each with $100. Then, we know in the
existing payment structure, the delivery driver would make
5 x 10 = $50 total.

Scenario 2
Let there be 10 orders, each with $100. Then, we know in the new
payment structure, the delivery driver would make
2.5 x 10 + 50 x 2 = $125.

While in the example above, we see that Scenario 1 wins in terms
of less payment, consider if each othe orders was $1,000,000.
Then, the payout would be $500,000 vs $250100.

Thus, it is important to understand the average order amount
in order to fully make a decision on the success of the new
structure. If most orders end up being very large, Scenario 2
may be better.

## IMPROVEMENT TO SOLUTION:

We can actually plot the two scenarios to find where they
are equal after fixing the total number of orders.

_Add a business suggestion_

- In large cities where average order may be pricier, implement
  Scenario 2
- Rotate the pricing structure seasonally, with low times using
  Scenario 1 and high times using Scenario 2.
