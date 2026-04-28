class MinStack:

    def __init__(self):
        self.l1 = []
        return None
    def push(self, val: int) -> None:
        self.l1.append(val)
        return None

    def pop(self) -> None:
        self.l1.pop()
        return None

    def top(self) -> int:
        return self.l1[-1]

    def getMin(self) -> int:
        return min(self.l1)
