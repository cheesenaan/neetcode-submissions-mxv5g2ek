class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            total = numbers[lp] + numbers[rp]
            if total == target:
                return [lp+1, rp+1]
            if total > target:
                rp = rp - 1
            else:
                lp = lp + 1

        