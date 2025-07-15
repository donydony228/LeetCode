class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = Counter(s)
        tt = Counter(t)

        result = tt - ss

        return list(result.keys())[0]