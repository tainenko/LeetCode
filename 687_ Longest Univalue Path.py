'''
ven a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0

        def Length(root):
            if not root:
                return 0
            left = Length(root.left) if root.left else -1
            right = Length(root.right) if root.right else -1
            pl = 1 + left if left >= 0 and root.val == root.left.val else 0
            pr = 1 + right if right >= 0 and root.val == root.right.val else 0
            self.res = max(self.res, pl + pr)
            return max(pl, pr)

        Length(root)
        return self.res
