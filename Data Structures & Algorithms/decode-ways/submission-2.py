class Solution:
    def numDecodings(self, s: str) -> int:
        # dictionary ??  # 10 , 01  agar 2 / 1 kai next 0 so (20,10) compulsory
        # but 3 0 error 40 error ....
        # 01 02 also error what you can do is create a sub array and from a dup 
        #string x 

        if s[0] == "0":
            return 0
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s) :
                return 1
            if s[i] == "0":
                return 0
            ways = dfs(i+1)
            
            if i+1 < len(s) and 10<= int(s[i:i+2]) < 27:
                ways+=dfs(i+2)
            dp[i] = ways
            return ways

        return dfs(0)