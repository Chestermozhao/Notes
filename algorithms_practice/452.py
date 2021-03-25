class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 氣球問題，就是給你氣球水平座標
        # 你要射幾箭可以全部KO
        sorted_points = sorted(points, key=lambda x: x[1])
        for i in range(len(sorted_points)):
            if sorted_points[i] is None:
                continue
            try:
                j = i + 1
                while True:
                    if sorted_points[i] is None:
                        j += 1
                        continue
                    start, end = sorted_points[i]
                    _start, _end = sorted_points[j]
                    if _start <= end:
                        sorted_points[j] = None
                        j += 1
                    else:
                        break
            except IndexError:
                break
        return len(sorted_points) - sorted_points.count(None)
