class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # k values possible are [1:h]
        l, r = 1, max(piles)
        minK = float('inf')


        while l <= r:
            k = l + ((r-l)//2)
            hours = 0

            for i in piles:
                hours += math.ceil(i/k)

            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                # k too small, move right
                l = k + 1


        return minK



       


        



        