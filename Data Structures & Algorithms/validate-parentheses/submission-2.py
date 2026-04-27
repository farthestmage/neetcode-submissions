class Solution:
    def isValid(self, s: str) -> bool:
        l1=[]
        for i in s:
            if i in "})]":
                if len(l1) == 0:
                    return False
                a=l1.pop()
                if not ((i == "}" and a =="{") or (i == ")" and a == "(") or (i=="]" and a== "[")):
                    return False
            else:
                l1.append(i)
        if len(l1)!=0:
            return False
        return True