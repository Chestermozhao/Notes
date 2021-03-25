class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #count = 0
        # create pre sum array
        #pre_sum_lst = [0]
        #for i in range(len(nums)):
        #    pre_sum_lst.append(pre_sum_lst[i]+nums[i])
        #pre_sum_lst = pre_sum_lst[1:]
        # calculate subarray sum equals to k
        #for i in range(len(nums)):
        #    for j in range(i, len(nums)):
        #        if pre_sum_lst[j] - pre_sum_lst[i] + nums[i] == k:
        #            count += 1
        #return count
        hashmap = collections.defaultdict(int)
        cum_sum = 0
        hashmap[0] = 1
        cnt = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in hashmap:
                print("====", cum_sum - k, i)
                cnt += hashmap[cum_sum - k]
            hashmap[cum_sum] += 1
        return cnt
