class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def reverseWithStack(self):
        if self.head == None or self.head.next == None:
            return self.head

        allNodes = []
        temp = self.head

        while temp != None:
            allNodes.append(temp)
            temp = temp.next

        start = allNodes.pop()
        self.head = start

        while len(allNodes) > 0:
            start.next = allNodes.pop()
            start = start.next
        
        start.next = None

        self.print()

    def reverseWithPointers(self):
        if self.head == None or self.head.next == None:
            return self.head

        prev = None
        curr = self.head
        next = self.head.next

        while next != None:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next

        curr.next = prev

        self.head = curr

        self.print()

    def print(self):
        temp = self.head

        while temp != None:
            print(temp.value)
            temp = temp.next
    
    def middleNode(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if self.head == None or self.head.next == None:
            return self.head

        slow = self.head
        fast = self.head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
