class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val

class Tree:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def getTree(self, tree):
        if tree == None:
            return [None]
        return [tree.val] + self.getTree(tree.left) + self.getTree(tree.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.getTree(p) == self.getTree(q)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root

    def bstHelperArray(self, root):
        """
        :type root: TreeNode
        :rtype: tupe: <boolean, array>
        """
        if root == None:
            return (True, [])

        leftTree = self.bstHelperArray(root.left)
        rightTree = self.bstHelperArray(root.right)

        if leftTree[0] == False or rightTree[0] == False:
            return (False, [])

        if (len(leftTree[1]) > 0 and root.val <= max(leftTree[1])) \
                or (len(rightTree[1]) > 0 and root.val >= min(rightTree[1])):
            return (False, [])

        returnArray = [root.val] + leftTree[1] + rightTree[1]
        return (True, returnArray)

    def bstHelperVars(self, root):
        """
        :type root: TreeNode
        :rtype: tupe: <boolean, int (max), int (min)>
        """
        if root == None:
            return (True, None, None)

        leftTree = self.bstHelperVars(root.left)
        rightTree = self.bstHelperVars(root.right)

        if leftTree[0] == False or rightTree[0] == False:
            return (False, 0, 0)

        if (leftTree[1] != None and root.val <= leftTree[1]) \
                or (rightTree[2] != None and root.val >= rightTree[2]):
            return (False, 0, 0)

        maxVal = 0
        minVal = 0

        validLeftMin = leftTree[2] != None
        validRightMin = rightTree[2] != None

        validLeftMax = leftTree[1] != None
        validRightMax = rightTree[1] != None

        if not validLeftMax and not validRightMax:
            maxVal = root.val
        else:
            if not validLeftMax and validRightMax:
                maxVal = max(root.val, rightTree[1])
            elif validLeftMax and not validRightMax:
                maxVal = max(root.val, leftTree[1])
            else:
                maxVal = max(root.val, leftTree[1], rightTree[1])

        if not validLeftMin and not validRightMin:
            minVal = root.val
        else:
            if not validLeftMin and validRightMin:
                minVal = min(root.val, rightTree[2])
            elif validLeftMin and not validRightMin:
                minVal = min(root.val, leftTree[2])
            else:
                minVal = min(root.val, leftTree[2], rightTree[2])
        return (True, maxVal, minVal)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        valid = self.bstHelperVars(root)
        return valid[0]
