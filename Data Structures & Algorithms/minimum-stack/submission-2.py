class MinStack:

    def __init__(self):
        self.l1 =[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.l1.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))

    def pop(self) -> None:
        self.l1.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.l1[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
