class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        # 條件2: 必須包含相同的字符集合
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        
        # 條件3: 字符頻率的分布必須相同
        return sorted(counter1.values()) == sorted(counter2.values())