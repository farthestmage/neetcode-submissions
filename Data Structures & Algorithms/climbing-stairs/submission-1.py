class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] *n
        def recurr(a):
            if a == n:
                return 1
            elif a>n:
                return 0
            if cache[a] != -1:
                return cache[a]
            
            cache[a]=recurr(a+1) + recurr(a+2)
            return cache[a]
        return recurr(0)