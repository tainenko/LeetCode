'''
ee, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return 0
        que = [root]
        while (que):
            nque = []
            for node in que:
                if node.left:
                    nque.append(node.left)
                if node.right:
                    nque.append(node.right)
            depth += 1
            que = nque
        return depth

#recursion solution
class Solution2:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))