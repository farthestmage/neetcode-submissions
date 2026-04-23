class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1 
        arr=[]
        target=min(heights)*(len(heights)-1)
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            if area<target:
                if heights[left]>heights[right]:
                    right-=1
                else:
                    left+=1
            elif area>=target:
                arr.append(area)
                if heights[left]>heights[right]:
                    right-=1
                else:
                    left+=1
        return max(arr)