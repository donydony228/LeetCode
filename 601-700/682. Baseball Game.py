class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = []

        for i in operations:
            if i == "+":
                result.append((int(result[-2]) + int(result[-1])))
            elif i == "D":
                result.append(int(result[-1]) * 2)
            elif i == "C":
                result.pop()
            else:
                result.append(i)
            # print(result)
        total = 0
        
        for i in result:
            total += int(i)
        
        return total