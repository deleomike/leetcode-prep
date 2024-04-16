

class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        old_min = self.getMin()
        minimum = min(val, old_min) if old_min is not None else val
        pair = (val, minimum)
        self.data.append(pair)
        
    def pop(self) -> None:
        return self.data.pop()[0]
        
    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        if len(self.data) == 0:
            return None

        return self.data[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()