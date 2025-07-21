class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                two = stack.pop()
                one = stack.pop()
                if i == "+":
                    result = one + two
                elif i == "-":
                    result = one - two
                elif i == "*":
                    result = one * two
                else:
                    result = int(one / two)
                stack.append(result)
            else:
                stack.append(int(i))
            print(i, stack)
        return stack[0]