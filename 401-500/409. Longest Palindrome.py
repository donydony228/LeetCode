class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = Counter(s)
        
        odd = False
        result = 0

        for i in ss.keys():
            if ss[i] % 2 == 1:
                odd = True 
            result += (ss[i]//2)*2
        return result + 1 if odd else result