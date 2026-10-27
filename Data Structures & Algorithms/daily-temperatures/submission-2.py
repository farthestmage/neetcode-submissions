class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # daily temperaturesss 
        # how to do append the index to a stack check for present temperature
        #if the present temperature is smaller than the future aka not warmer
        # pop till that temperature is cooler than present and than append to the 
        #array

        l1 = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
            while len(stack)!=0 and  temperatures[stack[-1]] < temperatures[i]:
                t = stack.pop()
                l1[t] = i-t
            stack.append(i)
        return l1
