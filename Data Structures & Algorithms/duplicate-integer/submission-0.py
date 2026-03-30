class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 9.19 pm
        distinct_nums = set(nums) #O(n) time and space

        d = {}
        for num in distinct_nums: #O(n) time and space
            d[num] = 0
        
        print(d)

        for num in nums: #O(n)
            d[num] += 1 #O(1)
            if d[num] >= 2:
                return True

        print(d)

        return False
        

         