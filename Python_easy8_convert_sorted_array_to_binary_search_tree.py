# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)

    def sortedArrayToBSTHelper(self, nums, left, right):
        if left > right:
            return None

        # Choose the middle element as the root
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBSTHelper(nums, left, mid - 1)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, right)

        return root

# Example usage:
# nums = [1, 2, 3, 4, 5, 6, 7]
# solution = Solution()
# root = solution.sortedArrayToBST(nums)
        