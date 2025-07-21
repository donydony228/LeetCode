class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        def check(s: str) -> str:
            string = []
            last = None

            for i in s:
                if not last:
                    last = i
                    string.append(i)
                elif i == last:
                    string.pop()
                    last = string[-1] if string else None
                else:
                    string.append(i)
                    last = i
                # print(i, string)
            return "".join(string)
        return check(s)