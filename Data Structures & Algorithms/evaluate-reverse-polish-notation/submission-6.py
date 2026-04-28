import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # something like this 
        # append the int value also convert them to int
        #ALso check if operator is hit pop two elements perform the operation put them back in the stack
        opr = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":lambda a, b: int(a/ b)}
        stack = []
        for i in tokens:
            if i in opr:
                a= stack.pop()
                b= stack.pop()
                stack.append(opr[i](b,a))
            else:
                stack.append(int(i))
        return stack[-1]