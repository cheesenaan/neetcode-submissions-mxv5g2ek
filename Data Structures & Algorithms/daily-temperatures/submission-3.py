class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]
        print("res is", res)

        for i in range(0, len(temperatures)):
            counter = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    counter = counter + 1
                    res[i] = counter
                    break
                else:
                    counter = counter + 1

        return res
            

        