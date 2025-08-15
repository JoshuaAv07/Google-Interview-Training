from node import StackNode as Node
from structure import Structure

class Stack(Structure):
    def __init__(self):
        self._top = None
        self._size = 0
        
    def top(self):
        if self._top:
            return self._top.data
        else:
            return "Empty"
        
    def clear(self):
        self._top = None
        self._size = 0
        
    def iter(self):
        current = self._top
        
        while current:
            yield current.data
            current = current.prev
            
    
    def push(self, data):
        node = Node(data)
        node.prev = self._top
        self._top = node            
        self._size += 1
        
    def pop(self):
        if self._top == None:
            return "Empty"
            
        else:
            top = self._top
            self._top = self._top.prev
            self._size -= 1
            return top.data