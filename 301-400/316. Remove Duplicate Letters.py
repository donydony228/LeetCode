class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        used = set()
        stack = []

        for i in s:
            count[i] -= 1

            if i in used:
                continue

            while stack and stack[-1] > i and count[stack[-1]] > 0:
                removed = stack.pop()
                used.remove(removed)
            stack.append(i)
            used.add(i)
            # print(i, count, used, stack)
        
        return ''.join(stack)