class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=[]
        for i in s:
            if i.isalnum():
                check.append(i.lower())
        left,right=0,len(check)-1
        while left<right:
            if check[left]!= check[right]:
                return False
            left+=1
            right=right-1
        return True