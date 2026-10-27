import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l1 = []
        opr = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":lambda a, b: int(a/ b)}
        for i in tokens:
            if i in opr:
                a= int(l1.pop())
                b = int(l1.pop())
                l1.append(opr[i](b,a))
            else:
                l1.append(i)
        return int(l1.pop())