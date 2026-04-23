class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s
        for i in range (len(s)):    
            if not  s[i].isalnum():
                res=res.replace(s[i],"")
        if res.replace(" ","").lower() == res.replace(" ","").lower()[::-1]:
            return True
        return False