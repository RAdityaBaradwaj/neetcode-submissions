class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix)*len(matrix[0])

        result = []

        m,n = 0,1
        k = 0
        i,j = 0,0

        while len(result) < total:
            print(i,j)
            print(result)
            result.append(matrix[i][j])
            if i == k and j == len(matrix[0]) - k-1 and m == 0 and n == 1:
                m = 1
                n = 0
            elif i == len(matrix) - k-1 and j == len(matrix[0]) - k-1 and m ==1 and n == 0:
                m = 0
                n = -1
            elif i == len(matrix) - k-1 and j == k and m == 0 and n == -1:
                m = -1
                n = 0
            elif i == k +1 and j == k and m == -1 and n == 0:
                m = 0
                n = 1
                k+=1
            i+=m
            j+=n

        return result