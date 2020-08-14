# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST(object):
    def isValidBstHelper(self, root, min, max):
        if root is None:
            return True
        
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False
        
        return self.isValidBstHelper(root.left, min, root.val) \
            and self.isValidBstHelper(root.right, root.val, max)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        valid = self.isValidBstHelper(root, None, None)
        return valid