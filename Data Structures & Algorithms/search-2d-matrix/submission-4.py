class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        
        row = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > target:
                row = i-1
                break

        print("row to search is  ", row)

        def binarySearch(l, r):
            if l > r:
                return False

            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                return binarySearch(l, m-1)
            elif matrix[row][m] < target:
                return binarySearch(m+1,r)


        return binarySearch(0, len(matrix[row])-1)

        
        
       