'''

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []

        def helper(node, left, res):
            if not node:
                return
            if not node.left and not node.right and left:
                res.append(node.val)
            if node.left:
                helper(node.left, True, res)
            if node.right:
                helper(node.right, False, res)

        if not root:
            return 0
        helper(root, False, res)

        return sum(res)