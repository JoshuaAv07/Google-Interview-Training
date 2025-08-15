from node import QueueNode as Node
from structure import Structure

class Queue(Structure):
    
    def __init__(self):
        super().__init__()
        
    def push_back(self, data):
        new_node = Node(data)
        
        # If it is empty, front and tail are the new node
        if self._tail == None:
            self._front = new_node
            self._tail = new_node
        # The next value of the tail is now the new tail
        else:
            self._tail.next = new_node
            self._tail = new_node
            
        self._size += 1
        
    def pop(self):
        if self._front == None:
            return "Empty"
        
        current = self._front
        self._front = current.next

        # Queue is now empty
        if self._front == None:
            self._tail = None
            
        self._size -= 1
        
        return current.data
        