class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = reversed(s)
        # t = reversed(t)
        ss = []
        tt = []

        for i in s:
            if i == "#":
                if ss:
                    ss.pop()
            else:
                ss.append(i)
        for i in t:
            if i == "#":
                if tt:
                    tt.pop()
            else:
                tt.append(i)
        return ss == tt