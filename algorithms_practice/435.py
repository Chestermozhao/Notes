class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先判斷是不是有貪心選擇性質
        # 也就是說，子問題最優的集合就是全局最優
        count = 0
        while any(intervals):
            # 找最小的結束區間，然後刪掉跟他重複的人，重複做就可以算出刪除幾次
            latest_end_inv, latest_end_idx = self.get_latest_end_inv(intervals)
            # 跟這個重疊的都remove -> count++
            start, end = intervals[latest_end_idx]
            intervals[latest_end_idx] = None
            for i, item in enumerate(intervals):
                if item is None:
                    continue
                _start, _end = item
                if _start < end:
                    intervals[i] = None
                    count += 1
        return count
        
    def get_latest_end_inv(self, intervals):
        latest_end_inv = -1
        latest_end_idx = -1
        for i, inv in enumerate(intervals):
            if inv is None:
                continue
            start, end = inv
            if latest_end_inv == -1:
                latest_end_inv = end
                latest_end_idx = i
            elif latest_end_inv > end:
                latest_end_inv = end
                latest_end_idx = i
        return latest_end_inv, latest_end_idx
