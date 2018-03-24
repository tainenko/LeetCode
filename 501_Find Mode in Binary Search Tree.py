'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = {}

        def helper(root, res):
            if not root:
                return
            helper(root.left, res)
            res[root.val] = res.get(root.val, 0) + 1
            helper(root.right, res)

        if not root:
            return []
        helper(root, res)
        mx = max(res.values())
        return [x for x in res if res[x] == mx]


class Solution2:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(root, pre, count, mx, res):
            if not root:
                return pre, count, mx
            pre, count, mx = inorder(root.left, pre, count, mx, res)
            if pre:
                if pre.val == root.val:
                    count += 1
                else:
                    count = 1
            if count > mx:
                mx = count
                del res[:]
                res.append(root.val)
            elif count == mx:
                res.append(root.val)
            return inorder(root.right, root, count, mx, res)

        if not root:
            return []
        res = []
        inorder(root, None, 1, 0, res)
        return res
