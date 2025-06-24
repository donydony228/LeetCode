# Write your MySQL query statement below
SELECT e2.name
FROM Employee e1
JOIN Employee e2 on e1.managerId = e2.id
GROUP BY e2.id
HAVING COUNT(*) >=5

# 這裡要寫 COUNT(*) >=5 不能寫 COUNT(e1.id) >=5
# 因為 e1.id 可能會有 NULL 的情況，COUNT(e1.id) 會忽略 NULL 值