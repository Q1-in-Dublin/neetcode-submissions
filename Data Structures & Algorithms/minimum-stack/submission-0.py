class MinStack:

    def __init__(self):
        self.b_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.b_stack.append(val)
        if not self.min_stack:  # min_stack is empty
            self.min_stack.append(val)

        elif val < self.min_stack[-1]:
            self.min_stack.append(val)

        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self) -> None:
        self.b_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.b_stack[-1]
        
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
