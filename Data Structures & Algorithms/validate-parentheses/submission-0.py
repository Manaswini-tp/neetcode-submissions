class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(':
                stack.append('(')
            elif c=='[':
                stack.append('[')
            elif c=='{':
                stack.append('{')
            else:
                if len(stack)==0:
                    return False
                if c==')' and stack[-1]=='(':
                    stack.pop()
                elif c==']' and stack[-1]=='[':
                    stack.pop()
                elif c=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
