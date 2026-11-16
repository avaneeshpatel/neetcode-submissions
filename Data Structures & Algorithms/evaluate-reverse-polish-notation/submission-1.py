class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+","-","*","/")
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                op2 = int(stack.pop(-1))
                op1 = int(stack.pop(-1))
                if token == "+":
                    ans = op1 + op2
                elif token == "-":
                    ans = op1 - op2
                elif token == "*":
                    ans = op1 * op2
                else:
                    ans = op1 / op2
                stack.append(ans)
        return int(stack[-1])
        