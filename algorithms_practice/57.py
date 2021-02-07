"""57. Insert Interval Medium
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_start = newInterval[0]
        new_end = newInterval[1]
        answer = []
        for i, item in enumerate(intervals):
            start = item[0]
            end = item[1]
            # 新的起點在區間之內
            if end < new_start:
                answer.append(item)
                # 如果已經最後一個，那這時候要順手加上new_interval
                if i == len(intervals) -1:
                    answer.append([new_start, new_end])
                continue
            elif start > new_end:
                if not answer or answer[-1][-1] < new_end:
                    answer.append([new_start, new_end])
                answer.append(item)
                continue
            new_start = start if start < new_start else new_start
            new_end = end if end > new_end else new_end
            # 如果已經最後一個，那這時候要順手加上new_interval
            if i == len(intervals) -1:
                answer.append([new_start, new_end])
        return answer
