'''
ee and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        target = set()

        def find(root, k, target):
            if not root:
                return False
            if root.val in target:
                return True
            else:
                target.add(k - root.val)
                return find(root.left, k, target) or find(root.right, k, target)

        return find(root, k, target)

class Solution2:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        target=set()
        q=[root]
        while q:
            curr=q.pop(0)
            if curr.val in target:
                return True
            else:
                target.add(k-curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False