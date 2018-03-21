'''
iven two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(s, t):
            if not s or not t:
                return not s and not t
            if s.val != t.val:
                return False
            return helper(s.left, t.left) and helper(s.right, t.right)

        if not s:
            return False
        if helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
