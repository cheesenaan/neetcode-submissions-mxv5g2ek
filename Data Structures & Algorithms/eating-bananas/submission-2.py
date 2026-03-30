class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        l, r = 1, max(piles)
        minK = max(piles)

        while l <= r:
            if l > r:
                break

            m = l + ((r-l) // 2) # prevent overflow

            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / m)
            
            if hours <= h:
                minK = min(minK, m)
                # search to left
                r = m - 1
            elif hours > h:
                # search to right
                l = m + 1

        return minK
        

            
            

        