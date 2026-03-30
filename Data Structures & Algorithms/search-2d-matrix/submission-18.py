class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        target_row = -1

        t, b = 0, rows-1

        while t <= b:

            m = t + ((b-t) // 2)
            if matrix[m][0] <= target <= matrix[m][-1]:
                target_row = m
                break
            elif target > matrix[m][-1]:
                # move down
                t = m + 1
            elif target < matrix[m][0]:
                # move up
                b = m - 1

        if target_row == -1:
            return False
        
        print("target row is ", target_row)

        l, r = 0 , cols

        while l <= r:
            m = l + ((r-l) // 2)
            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] > target:
                # search left
                r = m - 1
            elif matrix[target_row][m] < target:
                # search right
                l = m + 1


        return False
        
        