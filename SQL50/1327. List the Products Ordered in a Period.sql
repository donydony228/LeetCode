# Write your MySQL query statement below
SELECT P.product_name, SUM(O.unit) AS unit
FROM Orders O
LEFT JOIN Products P ON O.product_id = P.product_id 
WHERE O.order_date BETWEEN '20200201' AND '20200229'
GROUP BY P.product_name
HAVING SUM(O.unit) >= 100