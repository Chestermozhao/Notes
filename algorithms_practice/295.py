"""Find Median from Data Stream
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def addNum(self, num: int) -> None:
        self.q.append(num)
        self.q.sort()
        
    def findMedian(self) -> float:
        if not len(self.q) % 2:
            pre_i = len(self.q)//2-1
            next_i = pre_i + 1
            return (self.q[pre_i] + self.q[next_i])/2
        else:
            return self.q[int((len(self.q)+1)/2)-1]


"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s_q = []
        self.l_q = []
        

    def addNum(self, num: int) -> None:
        if not self.s_q or num <= max(self.s_q):
            self.s_q.append(num)
            self.s_q.sort()
        else:
            self.l_q.append(num)
            self.l_q.sort()
  
        if len(self.s_q) < len(self.l_q):
            self.s_q.append(self.l_q.pop(0))
            self.s_q.sort()
        elif len(self.s_q) - len(self.l_q) == 2:
            self.l_q.append(self.s_q.pop())
            self.l_q.sort()
        
    def findMedian(self) -> float:
        if len(self.s_q) > len(self.l_q):
            return self.s_q[-1]
        else:
            return (self.s_q[-1] + self.l_q[0]) / 2
"""
