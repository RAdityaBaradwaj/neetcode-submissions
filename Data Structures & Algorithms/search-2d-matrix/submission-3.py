class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0,len(matrix)-1
        mid = 0
        while left < right:
            mid = (left+right)//2
            print(matrix[mid][0],mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid+1
        currRow = left
        left,right = 0,len(matrix[0])-1
        while left <= right:
            mid = (left+right)//2
            if matrix[currRow][mid] == target:
                return True
            elif matrix[currRow][mid] > target:
                right = mid-1
            else:
                left = mid+1
        if currRow > 0:
            currRow = currRow-1
            left,right = 0,len(matrix[0])-1
            while left <= right:
                mid = (left+right)//2
                if matrix[currRow][mid] == target:
                    return True
                elif matrix[currRow][mid] > target:
                    right = mid-1
                else:
                    left = mid+1

        return False

                
