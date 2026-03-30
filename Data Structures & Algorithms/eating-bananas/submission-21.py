class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        minK = max(piles)


        while l <= r:
            k = l + ((r-l)//2)

            hours = 0
            for i in piles:
                hours += math.ceil(i/k)

            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1

        return minK




        



        