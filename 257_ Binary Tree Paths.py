'''

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        q = [(root, '')]
        while q:
            root, ls = q.pop(0)
            if not root.left and not root.right:
                res.append(ls + str(root.val))
            if root.left:
                q.append((root.left, ls + str(root.val) + '->'))
            if root.right:
                q.append((root.right, ls + str(root.val) + '->'))
        return res
