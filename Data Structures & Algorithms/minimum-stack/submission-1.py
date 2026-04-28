class MinStack:

    def __init__(self):
        self.l1 = []
        self.minStack = []
        return None
    def push(self, val: int) -> None:
        self.l1.append(val)
        if not self.minStack or self.minStack[-1]>=val:
            self.minStack.append(val)
        return None

    def pop(self) -> None:
        pop = self.l1.pop()
        if self.minStack[-1] == pop:
            self.minStack.pop()
        return None

    def top(self) -> int:
        return self.l1[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
