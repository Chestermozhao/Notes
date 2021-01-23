class Solution:
    def count_zeros(self,num):
        d=5
        zeros=0
        while d<=num:
            zeros+=num//d
            d*=5
        return zeros
		
    def preimageSizeFZF(self, K: int) -> int:
        start=0
        # 5 * 10**9
        end=int(5e9)
        while start<=end:
            # get mid for b-search
            mid=start+(end-start)//2
            print("====mid====", start, end)
            # actually this method is count 5 numbers from 0 to mid
            temp=self.count_zeros(mid)
            print("===tmp===", temp)
            # 因為每遇到一次5, 0的數量就會上去，所以每個k如果有0，就是5，否則就沒有
            if temp==K:
                return 5
            if temp>K:
                end=mid-1
            else:
                start=mid+1
        return 0
