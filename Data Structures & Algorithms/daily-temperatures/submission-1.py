class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                
                if temperatures[j] <= temperatures[i]:
                    count = count + 1
                else:
                    print("temperatures[j]", temperatures[j])
                    print("temperatures[i]", temperatures[i])
                    count = count + 1
                    res[i] = count
                    break

        return res




        