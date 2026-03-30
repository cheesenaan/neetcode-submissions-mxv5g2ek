class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l , r = 1, max(piles)
        minK = r

        while l <= r:
            if l > r:
                return minK

            k = l + ((r-l) // 2) # prevent overflow

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                minK = min(minK, k)
                # search right
                r = k - 1
            elif hours > h:
                # search right 
                l = k + 1

        return minK



