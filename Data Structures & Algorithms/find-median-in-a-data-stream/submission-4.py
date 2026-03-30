class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        return 

    def findMedian(self) -> float:
        # if odd take the middle value
        if (len(self.arr) % 2) != 0:
            length = len(self.arr)
            idx = length // 2
            return self.arr[idx]
        else:
            length = len(self.arr)
            idx = length // 2
            return  (self.arr[idx] + self.arr[idx-1]) / 2

        
        
        