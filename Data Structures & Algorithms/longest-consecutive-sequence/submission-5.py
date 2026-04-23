class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=sorted(list(set(nums)))
        count=defaultdict(list)
        res = []
        for i in num:
            if len(res)==0 or res[-1]+1==i:
                res.append(i)
            else:
                count[len(res)]=res
                res=[]
                res.append(i)
        
        count[len(res)] = res    
        return sorted(count.keys(),reverse= True)[0]
