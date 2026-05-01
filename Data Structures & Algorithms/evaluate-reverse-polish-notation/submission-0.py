class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        if tokens:
            stack= []
        else:
            return

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
                continue

            if t == "+":
                a = stack.pop()
                b = stack.pop()
                res= b+a
                stack.append(res)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                res= b-a
                stack.append(res)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                res= b*a
                stack.append(res)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                res= int(b/a)
                stack.append(res)

        return int(stack[-1])