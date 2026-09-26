class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        for i in s:
            if i != " " and i.isalnum():
                l = l + i.lower()
        left,right = 0,len(l)-1
        while left<right:
            if l[left] != l[right]:
                return False
            left+=1
            right-=1
        return True