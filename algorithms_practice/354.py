"""354 Russian Doll Envelopes
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0],-x[1]))
        nums = (y for x,y in sorted_envelopes)

        lis_list = []
        for num in nums:
            # 去找num在lis_list中的引數
            # 從小到大應該放置在哪個position
            pos = bisect_left(lis_list, num)
            # 如果position index == lenght of lis_list
            # 代表下一個比上一個大，他要插在最後的意思，所以就加上就好
            if pos == len(lis_list):
                lis_list.append(num)
            # 如果position index != lenght of lis_list
            # 代表下一個比較小，所以就把他應該差在哪裡替換過來
            else:
                lis_list[pos] = num
        # 最後會得到最小遞增長度
        return len(lis_list)
