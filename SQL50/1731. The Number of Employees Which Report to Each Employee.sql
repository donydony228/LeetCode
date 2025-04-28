# Write your MySQL query statement below
SELECT Employees.reports_to AS employee_id, e.name, COUNT(Employees.employee_id) AS reports_count, ROUND(AVG(Employees.age), 0) AS average_age
FROM Employees
JOIN Employees AS e 
ON Employees.reports_to = e.employee_id
WHERE Employees.reports_to IS NOT null
GROUP BY Employees.reports_to
ORDER BY Employees.reports_to