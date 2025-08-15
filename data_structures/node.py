class Node:
    def __init__(self, data):
        self.data = data
        
class ListNode(Node):
    def __init__(self, data, next = None):
        super().__init__(data)
        self.next = next
        
class DoubleNode(Node):
    def __init__(self, data, next = None, prev = None):
        super().__init__(data)
        self.next = next
        self.prev = prev
        
class StackNode(Node):
    def __init__(self, data, prev = None):
        super().__init__(data)
        self.prev = prev

class QueueNode(ListNode):
    def __init__(self, data, next = None):
        super().__init__(data, next)
        
class BinaryTreeNode(Node):
    def __init__(self, data, left = None, right = None):
        super().__init__(data)
        self.left = left
        self.right = right