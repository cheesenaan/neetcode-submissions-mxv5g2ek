class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        unique_elements = set(nums)

        hp = {}
        for n in unique_elements:
            hp[n] = 0

        for n in nums:
            hp[n] += 1

        print(hp)

        arr = []
        for i in range(0 , k):
            x =  max(hp, key=hp.get)
            print(x)
            arr.append(x)
            hp.pop(x)

        return arr
        