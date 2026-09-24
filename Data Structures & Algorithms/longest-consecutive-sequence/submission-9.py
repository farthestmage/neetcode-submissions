class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make set of nums #2,20,4,10,3,4,5
        # One solution sort the array and just simply check the next element soln 
        # O(nlogn)
        # But we need O(n)??
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num+length) in numset:
                    length+=1
                longest = max(longest,length)
        return longest