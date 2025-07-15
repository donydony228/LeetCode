class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        st = {}
        ts = {}

        for i in range(len(s)):
            chars, chart = s[i], t[i]

            if chars in st:
                if st[chars] != chart:
                    return False
            else: 
                st[chars] = chart

            if chart in ts:
                if ts[chart] != chars:
                    return False
            else: 
                ts[chart] = chars
        
        return True