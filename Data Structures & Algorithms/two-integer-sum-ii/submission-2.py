class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # WE know the array is sorted A is target -n logic simple
        #How do we know  it's 0{1} additional space is a doubt well
        left ,right = 0 ,len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if  sum == target:
                return[left+1,right+1]  
            elif sum > target:
                 right-=1
            elif sum<target:
                left+=1
        return[-1,-1]