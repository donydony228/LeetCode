class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == "1":
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # 結果列表
        result = []
        
        # 定義回溯函數
        def backtrack(index: int, current: str):
            # 如果當前字符串長度等於輸入數字的長度，表示找到一個完整組合
            if len(current) == len(digits):
                result.append(current)
                return
            
            # 獲取當前數字對應的所有可能字母
            letters = phone_map[digits[index]]
            # 對於每個可能的字母，進行遞迴
            for letter in letters:
                # 添加當前字母並繼續處理下一個數字
                backtrack(index + 1, current + letter)
        
        # 從第一個數字開始回溯
        backtrack(0, "")
        return result