# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class K_thSmallestInBST(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        heap = []
        self.buildHeap(root, heap)
        
        returnValue = None
        while k > 0:
            returnValue = heapq.heappop(heap)
            k -= 1
            
        return returnValue
        
    def buildHeap(self, root, heap):
        if not root:
            return
        
        heapq.heappush(heap, root.val)
        self.buildHeap(root.left, heap)
        self.buildHeap(root.right, heap)
        
    def kthSmallestBFS(self, root, k):
        heap = []
        nodes = [root]

        while len(nodes):
            curr = nodes.pop(0)
            if curr:
                heapq.heappush(heap, curr.val)

                nodes.extend([curr.left, curr.right])

        returnValue = None
        while k > 0:
            returnValue = heapq.heappop(heap)
            k -= 1
            
        return returnValue

    def kthSmallestInOrder(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        vals = self.inorder(root)
        return vals[k-1]
        
    def inorder(self, root):
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
