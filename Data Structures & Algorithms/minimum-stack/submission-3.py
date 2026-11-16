class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_ele = float('inf')

    def push(self, val: int) -> None:
        self.min_ele = min(self.min_ele,val)
        self.stack.append([val,self.min_ele])
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(-1)
        if len(self.stack) > 0:
            self.min_ele = self.stack[-1][1]
        else:
            self.min_ele = float('inf')

        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        
