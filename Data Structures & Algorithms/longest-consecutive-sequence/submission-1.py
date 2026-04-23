class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not  nums:
            return 0
        chec=list(set(nums))
        chec.sort()
        counts=[]
        count=1
        y=chec[0]
        for i in chec[1:] :
            if i != y+1:
                counts.append(count)
                count=0
            count+=1
            y=i
        counts.append(count)
        return max(counts)