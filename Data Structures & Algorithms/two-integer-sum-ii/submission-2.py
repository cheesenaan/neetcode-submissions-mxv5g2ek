class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lp, rp = 0 , len(numbers) - 1

        while lp < rp:
            n = numbers[lp] + numbers[rp]
            if n > target:
                rp = rp - 1
            elif n < target:
                lp = lp + 1
            else:
                return [lp+1,rp+1]

                


        