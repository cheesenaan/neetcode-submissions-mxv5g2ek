class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #binary search to find target_row

        if not matrix or not matrix[0]:
            return False

        target_row = -1
        l, r = 0, len(matrix) - 1

        while l <= r:

            m = l + ((r-l) // 2) # prevent overflow

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m -1
            else:
                target_row = m
                break

        if target_row == -1:
            return False

        l, r = 0, len(matrix[target_row]) - 1

        while l <= r:
            m = l + ((r-l) // 2) # prevent overflow

            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] > target:
                r = m - 1
            elif matrix[target_row][m] < target:
                l = m + 1


        return False

