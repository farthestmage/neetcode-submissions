class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Stack idea is create a stack work with while loop
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse =True)
        stack = []

        for i in (pair):
            stack.append((target-i[0])/i[1])
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)