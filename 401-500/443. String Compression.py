class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # 寫入位置
        read = 0   # 讀取位置
        
        while read < len(chars):
            # 當前處理的字符
            current_char = chars[read]
            
            # 計算連續重複字符的數量
            count = 0
            while read < len(chars) and chars[read] == current_char:
                count += 1
                read += 1
            
            # 先寫入字符
            chars[write] = current_char
            write += 1
            
            # 如果數量大於1，需要寫入數量
            if count > 1:
                # 將數字轉換為字符串，然後逐個字符寫入
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
        
        return write