class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        minK = r

        while l <=r :

            k = l + ((r-l) // 2)

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                minK = min(minK , k)
                # move left
                r = k - 1
            else:
                # move right
                l = k + 1

        return minK


            


       