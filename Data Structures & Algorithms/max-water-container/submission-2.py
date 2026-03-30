class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # find index difference in length between elements
        # choose the min between two elements and multiply with index difference

        # res = 0

        # for i in range(0, len(heights)):
        #     for j in range(i+1, len(heights)):
        #         index_diff = abs(j - i)
        #         min_height = min(heights[i], heights[j])
        #         volumne = index_diff * min_height
        #         res = max(res, volumne)

        # return res

        #O(n^2) time and O(1) space

        lp, rp = 0, len(heights)-1
        res = 0

        while lp < rp:
            index_diff = abs(lp - rp)
            min_height = min(heights[rp], heights[lp])
            volumne = index_diff * min_height
            res = max(res, volumne)

            if heights[rp] > heights[lp]:
                lp = lp + 1
            else:
                rp = rp - 1

        return res
        