class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # k_vales can be from [1, max(piles)]

        minK = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            k = l + ((r-l) // 2)

            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                minK = min(minK, k)
                # search left
                r = k - 1
            else:
                # search right
                l = k + 1

        return minK


            





        