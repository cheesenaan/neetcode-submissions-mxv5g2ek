from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] = the smallest possible ending value
        # of an increasing subsequence of length (i + 1)
        tails = []  # Space: O(n) in the worst case

        for num in nums:  # Loop runs n times → O(n)
            # Find the index where 'num' should go in tails
            # bisect_left does binary search on tails → O(log n)
            idx = bisect_left(tails, num)  

            if idx == len(tails):
                # num is larger than all elements in tails
                # → we can extend the longest increasing subsequence
                tails.append(num)  # O(1) amortized
            else:
                # Replace the element at idx with num
                # Keeps tails sorted and smaller endings → more room to grow
                tails[idx] = num  # O(1)

        # The length of tails is the length of the LIS
        return len(tails)  # O(1)

# Overall Time Complexity: O(n log n)
#   - For each of n elements, we do binary search → O(log n)
# Overall Space Complexity: O(n)
#   - tails can grow up to n in worst case
