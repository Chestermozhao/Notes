class Solution:
    def reverse_diff(self, diff):
        res = [0]*(len(diff))
        res[0] = diff[0]
        for i in range(len(diff)):
            res[i] = res[i-1] + diff[i]
        return res
        
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for i in range(len(bookings)):
            start, end, seats = bookings[i]
            diff[start-1] += seats
            diff[end] -= seats
        return self.reverse_diff(diff[:-1])
