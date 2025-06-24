# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country, 
        COUNT(amount) AS trans_count,
        -- state = 'approved' → 如果為真返回 1，為假返回 0，所以不能寫 COUNY 而是 SUM
        SUM(state = 'approved') AS approved_count, # 
        SUM(amount) AS trans_total_amount,
        SUM((state = 'approved')*amount) AS approved_total_amount

FROM Transactions
GROUP BY month, country