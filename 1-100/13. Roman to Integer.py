class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        value = []
        
        for i in s:
            value.append(roman[i])
        value.reverse()
        before = None

        for i in value:
            if not before:
                before = i
            
            if i >= before:
                total += i
            else:
                total -= i
            
            before = i
        
        return total
    
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        # 從右到左遍歷（不需要額外陣列）
        for i in range(len(s) - 1, -1, -1):
            current_value = roman[s[i]]
            
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            
            prev_value = current_value
        
        return total