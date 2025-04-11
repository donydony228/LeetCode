# Write your MySQL query statement below
SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15

# LENGTH 的寫法要看資料庫的版本
# MySQL 的寫法是 LENGTH
# PostgreSQL 的寫法是 CHAR_LENGTH
# SQLite 的寫法是 LENGTH
# SQL Server 的寫法是 LEN
# Oracle 的寫法是 LENGTH