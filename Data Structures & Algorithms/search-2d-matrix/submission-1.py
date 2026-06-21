class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0,len(matrix) - 1
        check = 0
        while left<=right:
            mid = left + (right-left) // 2
            
            if matrix[mid][0] == target:
                return True
                break 
            if matrix[mid][0] < target:
                check = mid
                left = mid + 1 
            else:
                right = mid - 1
        left,right = 0, len(matrix[check]) - 1
        while left<=right:
            mid = left + (right-left) // 2

            if matrix[check][mid] == target:
                return True
                break
            if matrix[check][mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return False 