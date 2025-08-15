class Structure:
    
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0
    
    def size(self):
        if self._tail == 0:
            return "Empty"
        return self._size
    
    def front(self):
        if self._front == None:
            return "Empty"
        return self._front.data
    
    def back(self):
        if self._tail is None:
            return "Empty"
        return self._tail.data
    
    def empty(self):
        if self._size == 0:
            return True
        else:
            False
    
    def clear(self):
        self._front = None
        self._tail = None
        self._size = 0
        
    def iter(self):
        current = self._front
        
        while current:
            data = current.data
            current = current.next
            yield data