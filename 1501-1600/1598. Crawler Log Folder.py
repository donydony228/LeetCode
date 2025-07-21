class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            if i =="../":
                if stack:
                    stack.pop()
                else:
                    continue
            elif i =="./":
                continue
            else:
                stack.append(i)
            print(i, stack)
        return len(stack)