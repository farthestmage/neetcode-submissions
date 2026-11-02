class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        stack = []
        res = []
        def checkPalindrome(st,en):
            while st<=en:
                if s[st] != s[en]:
                    return False
                st+=1
                en-=1
            
            return True

        def dfs(start):
            if start >= len(s):
                res.append(stack.copy())
                return
            
            for end in range(start,len(s)):
                if checkPalindrome(start,end):
                    stack.append(s[start:end+1])
                    dfs(end+1)
                    stack.pop()
            
        dfs(0)
        return res