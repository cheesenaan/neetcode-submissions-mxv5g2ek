class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        answer = {}
        for i in range(0, len(nums)):
            answer[i+1] = []

        for num, count in counts.items():
            answer[count].append(num)

        res = []
        for i in range(len(answer), 0, -1):
            print(i, answer[i])
            if answer[i]:
                for x in answer[i]:
                    res.append(x)
            if len(res) == k:
                return res

        return res
        