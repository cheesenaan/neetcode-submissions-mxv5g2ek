class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # find index difference in length between elements
        # choose the min between two elements and multiply with index difference

        arr = []

        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                index_diff = abs(j - i)
                min_height = min(heights[i], heights[j])
                volumne = index_diff * min_height
                arr.append(volumne)

        return max(arr)
        