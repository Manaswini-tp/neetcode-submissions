class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
    def push(self, val: int) -> None:
        self.min_val = min(val, self.min_val)
        self.stack.append([val, self.min_val])

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)!=0:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = float('inf')        

    def top(self) -> int:
        top_val = self.stack[-1][0]
        return top_val

    def getMin(self) -> int:
        a = self.stack[-1][1]
        return a
