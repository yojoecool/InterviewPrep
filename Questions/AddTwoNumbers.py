# https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnValue = ListNode(0)
        if not l1 and not l2: return None
        
        if l1 and l2:
            returnValue.val = l1.val + l2.val
            returnValue.next = self.addTwoNumbers(l1.next, l2.next)
        elif not l1:
            returnValue.val = l2.val
            returnValue.next = self.addTwoNumbers(None, l2.next)
        elif not l2:
            returnValue.val = l1.val
            returnValue.next = self.addTwoNumbers(l1.next, None)
            
        if returnValue.val >= 10:
            returnValue.val -= 10
            if returnValue.next:
                returnValue.next.val += 1
            else:
                returnValue.next = ListNode(1)
                
        n = returnValue
        while n:
            if n.val >= 10:
                n.val -= 10
                
                if n.next:
                    n.next.val += 1
                else:
                    n.next = ListNode(1)
                    
            n = n.next
            
        return returnValue
        