# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Move to the starting point
        for i in range(1, left):
            pre = pre.next

        # Reverse the sublist from left to right
        current = pre.next
        next_node = None
        prev = None

        for i in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Connect the reversed sublist back to the main list
        pre.next.next = current
        pre.next = prev

        return dummy.next
        