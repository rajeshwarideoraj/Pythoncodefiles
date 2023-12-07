# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       # Create a dummy node to simplify code
        dummy = ListNode(-1)
        current = dummy

        # Iterate through both lists until one of them is exhausted
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If any list is not exhausted, append the remaining nodes
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        # The merged list starts from the next of the dummy node
        return dummy.next 