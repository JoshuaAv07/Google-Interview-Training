class MinHeap:
    
    def __init__(self):
        self._heap = []
        
    # Defined operations for getting parent, and children nodes
    def parent(self, index):
        return (index - 1) // 2
    
    def left(self, index):
        return 2 * index + 1
    
    def right(self, index):
        return 2 * index + 2
    
    # Exchange 1 value for another (i to j, and j to i)
    def swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        
    def insert(self, data):
        self._heap.append(data)
        # Bubble it up until the heap property is restored
        self.heapify_up(len(self._heap) - 1)
        
    def heapify_up(self, index):
        # Swap the new element with its parent while it's smaller
        while index > 0 and self._heap[index] < self._heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
            
    def extract_min(self):
        # If empty
        if not self._heap:
            return None
        # If only one element
        if len(self._heap) == 1:
            return self._heap.pop()
        
        root = self._heap[0] # Saving min value
        self._heap[0] = self._heap.pop() # Move last element to root
        self.heapify_down(0) # Restore heap structure
        return root
    
    def heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)
        
        # If left is smallest than the parent, the smallest is left
        if left < len(self._heap) and self._heap[left] < self._heap[smallest]:
            smallest = left
        # If right is smallest than the parent, the smallest is right
        if right < len(self._heap) and self._heap[right] < self._heap[smallest]:
            smallest = right
        
        # If smallest is not the index swap index and smallest, and continue heapifying down
        if smallest !=  index:
            self.swap(index, smallest)
            self.heapify_down(smallest)
            
    def peek(self):
        return self._heap[0] if self._heap else None
    
    def __len__(self):
        return len(self._heap)
    
    def __str__(self):
        return str(self._heap)