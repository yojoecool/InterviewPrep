"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class N_aryTraversal(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        vals = {}
        self.levelOrderHelper(root, 0, vals)
            
        return vals.values()
        
        
    def levelOrderHelper(self, root, level, vals):
        if root is None: return
        
        if level not in vals:
            vals[level] = []
            
        vals[level].append(root.val)
        
        for child in root.children:
            self.levelOrderHelper(child, level + 1, vals)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        returnList = []
        if (root is None):
            return returnList
    
        returnList = [root.val]
        for node in root.children:
            returnList = returnList + self.preorder(node)
            
        return returnList