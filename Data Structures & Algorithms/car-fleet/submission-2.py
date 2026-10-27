class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a calculate destination reaching time if a car can arrive before the      
        #next one meaning they are in the same fleet from position i it takes   
        #car i to reach in 10 seconds car i-1 takes 5 hence 
        l1 =[]
        for pos,sp in zip(position,speed):
            l1.append([pos,sp])
        l1.sort(reverse = True)
        stack =[]
        for i in l1:
            time = (target-i[0])/i[1]
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)