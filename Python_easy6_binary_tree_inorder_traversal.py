# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorderTraversalHelper(root, result)
        return result

    def inorderTraversalHelper(self, node, result):
        if node is None:
            return

        # Traverse the left subtree
        self.inorderTraversalHelper(node.left, result)

        # Visit the current node
        result.append(node.val)

        # Traverse the right subtree
        self.inorderTraversalHelper(node.right, result)