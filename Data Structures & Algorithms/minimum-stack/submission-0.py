class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val>self.min_stack[-1]:
                self.min_stack.append(self.min_stack[-1])
                return None
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
