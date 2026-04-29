class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # last element always 0
        # Thought process how is confusing 
        stack = []
        res = [0 for _ in range (len(temperatures))]
        for i in range (len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res