class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        pres = -1

        def inorder(root, pres, res):
            if not root:
                return
            inorder(root.left, pres, res)
            if pres != -1:
                res.append(abs(pres - root.val))
            pres = root.val
            inorder(root.right, pres, res)

        inorder(root, pres, res)

        return min(res)