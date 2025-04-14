# Write your MySQL query statement below
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
WHERE transaction_id is null
GROUP BY customer_id