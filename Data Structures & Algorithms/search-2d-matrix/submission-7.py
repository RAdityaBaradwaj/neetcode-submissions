class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0, len(matrix)-1

        while left < right:
            mid = (left+right+1)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
        
        currRow = left
        left,right = 0, len(matrix[0])-1
        while left <= right:
            mid = (left+right)//2
            if matrix[currRow][mid] == target:
                return True
            elif matrix[currRow][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False