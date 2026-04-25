class Solution:
    def isPalindrome(self, s: str) -> bool:            
        a=""
        for i in s:
            if i != " " and  (i.isalnum()):
                a += i.lower()
        if a =="":
            return True
        left ,right = 0 , len(a)-1

        while left <= right:
            if a[left] != a[right]:
                return False
            left+=1
            right-=1
        return True