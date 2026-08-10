class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                a = int(c)
                stack.append(a)
            else:
                a = stack.pop()
                b = stack.pop()
                match c:
                    case "+":
                        res = a+b
                        stack.append(res)
                    case "*":
                        res = a*b
                        stack.append(res)
                    case "/":
                        res = int(b/a)
                        stack.append(res)
                    case "-":
                        res = b-a
                        stack.append(res)
                    case _ :
                        break
        res = stack.pop()
        return res

        
