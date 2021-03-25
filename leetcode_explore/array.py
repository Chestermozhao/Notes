class Solution:
    # 485
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cum_sum = 0
        seg_lst = []
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                cum_sum += 1
            else:
                seg_lst.append(cum_sum)
                cum_sum = 0
        if nums[-1] != 0:
            seg_lst.append(cum_sum)
        return max(seg_lst)

    # 1295
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt

    # 977
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2 
                i += 1
            else:
                res[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return res

    # 1346
    def checkIfExist(self, arr: List[int]) -> bool:
        is_exist = False
        for i in range(len(arr)):
            num = arr[i]
            if num == 0:
                if arr.count(0) > 1:
                    return True
                continue
            if num % 2 == 0:
                if arr.count(num//2):
                    return True
        return is_exist

    # 941
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
