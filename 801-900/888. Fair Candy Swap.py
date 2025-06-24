class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        delta = (sum(bobSizes) - sum(aliceSizes)) // 2

        setB = set(bobSizes)

        for a in aliceSizes:
            if a + delta in setB:
                return [a, a + delta]

        return [] 
    

# 詳細解釋

# 計算總數：首先，我們計算 Alice 和 Bob 各自擁有的糖果總數 sumA 和 sumB。
# 計算差值：要使交換後兩人糖果總數相同，我們需要找到一個公式。假設：

# Alice 給出含有 x 個糖果的盒子，並收到含有 y 個糖果的盒子
# Bob 給出含有 y 個糖果的盒子，並收到含有 x 個糖果的盒子

# 交換後的總數相等，可以表示為：
# sumA - x + y = sumB - y + x
# 整理此等式：
# sumA - x + y = sumB - y + x
# sumA + 2y - 2x = sumB
# 2y - 2x = sumB - sumA
# y - x = (sumB - sumA) / 2
# y = x + (sumB - sumA) / 2
# 所以 delta = (sumB - sumA) / 2 是關鍵計算值。
# 快速查找：我們將 Bob 的糖果盒尺寸轉換為集合（set），這樣可以在 O(1) 時間內查找特定值。
# 尋找匹配：對於 Alice 的每個糖果盒 a，我們檢查 Bob 是否有一個糖果盒包含 a + delta 個糖果。如果找到了這樣的一對盒子，交換它們就能使 Alice 和 Bob 的糖果總數相等。

# 範例說明
# 以範例 aliceSizes = [1, 1] 和 bobSizes = [2, 2] 為例：

# sumA = 1 + 1 = 2
# sumB = 2 + 2 = 4
# delta = (4 - 2) // 2 = 1
# 我們需要找到 Alice 的一個盒子 a 和 Bob 的一個盒子 a + delta = a + 1
# 對於 Alice 的盒子 a = 1，檢查 Bob 是否有盒子 1 + 1 = 2
# Bob 確實有盒子 2，所以答案是 [1, 2]

# 時間和空間複雜度

# 時間複雜度：O(n + m)，其中 n 是 Alice 的盒子數量，m 是 Bob 的盒子數量。我們需要遍歷所有盒子並執行常數時間的查找。
# 空間複雜度：O(m)，用於存儲 Bob 的盒子大小集合。