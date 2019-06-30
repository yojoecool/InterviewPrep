class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, arr):
        if len(arr) == 0:
            self.head = None
        else:
            self.head = Node(arr[0])
            temp = self.head
            for num in arr[1:]:
                temp.next = Node(num)
                temp = temp.next

    """
    Assumption: range start - finish exist in linked list
    """
    def reverseRangeBridges(self, start, finish):
        if not self.head or not self.head.next:
            return self.head

        if start == 0:
            before = None
            prev = None
            curr = self.head
            next = curr.next
        else:
            before = self.head
            for _ in range(start - 1):
                before = before.next

            prev = before
            curr = before.next
            next = curr.next

        firstNode = curr

        for _ in range(start, finish + 1):
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = next.next

        firstNode.next = curr
        if before:
            before.next = prev
        else:
            self.head = prev

        self.print()

    # time complexity O(n)
    # space complexity O(n)
    def reverseRangeVivian(self, start, finish):
        if (self.head == None or self.head.next == None):
            return self.head
        counter = 0
        stack = []
        temp = self.head
        is_start = False
        while (counter < start - 1):
            temp = temp.next
            counter += 1
        begin = temp
        if (counter == start):
            stack.append(temp)
            is_start = True
        temp = temp.next
        counter += 1
        while (counter <= finish):
            stack.append(temp)
            temp = temp.next
            counter += 1
        end = temp
        while (len(stack) > 0):
            if (is_start):
                self.head = stack.pop()
                begin = self.head
                is_start = False
            else:
                begin.next = stack.pop()
                begin = begin.next
        begin.next = end
        return self.head

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

    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        if self.head == None or self.head.next == None:
            return False

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    """
    Get node at the start of the cycle.
    Use Floyd's algorithm (tortoise and hare) + math

    Explanation of algorithm: https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
    """
    def detectCycle(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if self.head == None or self.head.next == None:
            return None

        slow = self.head
        fast = self.head

        found = False

        while fast != None and fast.next != None and not found:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True

        if not found:
            return None

        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    """
    We are given head, the head node of a linked list containing unique integer values.

    We are also given the list G, a subset of the values in the linked list.

    Return the number of connected components in G,
    where two values are connected if they appear consecutively in the linked list.

    Example 1:

    Input:
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation:
    0 and 1 are connected, so [0, 1] and [3] are the two connected components.
    Example 2:

    Input:
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation:
    0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
    """
    def numComponents(self, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        x = set(G)
        currBuild = False

        components = 0
        head = self.head

        while head:
            if head.value in x:
                currBuild = True
            else:
                if currBuild > 0:
                    components += 1
                currBuild = False
            head = head.next

        if currBuild:
            components += 1
        return components
