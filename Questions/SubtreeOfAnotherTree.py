# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        sameRoot = self.findSameRoot(s, t)
        if not sameRoot:
            return False
        
        isSameTree = self.isSameTree(sameRoot, t)
        if isSameTree:
            return True
        
        isInLeft = self.isSubtree(s.left, t)
        if isInLeft:
            return True
        
        return self.isSubtree(s.right, t)
    
    def findSameRoot(self, s, t):
        if not s:
            return None
        if s.val == t.val:
            return s
        
        left = self.findSameRoot(s.left, t)
        
        if left:
            return left
        
        return self.findSameRoot(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        
        return s.val == t.val \
            and self.isSameTree(s.left, t.left) \
            and self.isSameTree(s.right, t.right)