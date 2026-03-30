class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search on first column to find target row
        t, b = 0, len(matrix)-1
        row = -1

        while t <= b:
            m = t +  ((b-t) // 2)

            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target > matrix[m][-1]:
                # search bottom
                t = m + 1
            else:
                # search top
                b = m - 1

        if row == -1:
            return False

        # binary search on target row
        

        l, r = 0, len(matrix[row])-1

        while l <= r:
            m = l + ((r-l) // 2)

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                # search left
                r = m - 1
            elif matrix[row][m] < target:
                # search right
                l = m + 1

        return False


        