# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Create a min-heap to store the nodes based on their values
        min_heap = []

        # Add the head nodes of all linked lists to the min-heap
        for lst in lists:
            if lst:
                heapq.heappush(min_heap, (lst.val, lst))

        # Dummy node to simplify code
        dummy = ListNode(-1)
        current = dummy

        # Process nodes from the min-heap
        while min_heap:
            # Get the node with the smallest value
            val, node = heapq.heappop(min_heap)

            # Add the node to the result list
            current.next = node
            current = current.next

            # Move to the next node in the selected list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))

        return dummy.next  # Return the merged sorted list
        