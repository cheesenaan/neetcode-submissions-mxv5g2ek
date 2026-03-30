class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        t, b = 0, len(matrix)-1
        row = -1

        while t <= b:
            m = t + ((b-t)//2) # prevent overflow

            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][0] > target:
                b = m - 1
            else:
                t = m + 1

        
        if row == -1:
            return False

        l, r = 0, len(matrix[row])-1

        while l <= r:
            m = l + ((r-l)//2)

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

