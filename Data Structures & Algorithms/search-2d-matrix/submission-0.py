class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:
            if self.binarySearch(arr, target) == True:
                return True

        return False


    def binarySearch(self, arr, target):

        l, r = 0 , len(arr)-1

        while l <= r:
            # mid = int((l+2)/2) # can lead to overflow
            mid = l + int((r-l)/2)

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid -1
            else:
                l = mid + 1

        return False
    