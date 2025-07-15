class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""
    
        # 遍歷映射表
        for value, symbol in roman_values:
            # 計算當前值可以使用多少次
            count = num // value
            # 將對應數量的符號添加到結果
            result += symbol * count
            # 從當前數中減去已經表示的值
            num %= value
        
        return result