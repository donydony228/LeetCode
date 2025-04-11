# Write your MySQL query statement below
SELECT name from Customer
WHERE referee_id != 2 or referee_id is null # 重點重點


-- 這是因為 SQL 使用三值邏輯（True、False 和 Unknown）處理 NULL 值。當你將 NULL 與任何值進行比較（即使是不等比較）
-- 時，結果都是 Unknown，而不是 True 或 False。SQL 的 WHERE 條件只會選擇計算結果為 True 的行，不會選擇結果為 
-- Unknown 的行。