# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # 142
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    # left and right pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                break
            elif _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
        return [left+1, right+1]
