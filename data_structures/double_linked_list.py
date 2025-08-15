from node import DoubleNode as Node
from structure import Structure

class DoublyLinkedList(Structure):
    def __init__(self):
        super().__init__()
     
    # Insert at the end
    def append(self, data):
        node = Node(data)
        
        # If Empty tail -> empty front = empty list
        if self._tail == None:
            self._front = node
            self._tail = node
        # If not empty, link the new to the tail = new tail
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
            
        self._size +=1
    
    def insertAfter(self, data, prev_to):
        # Make sure the previous node exists
        if prev_to == None:
            print("CANNOT be NULL")
            return
        
        new_node = Node(data)
        new_node.next = prev_to.next
        new_node.prev = prev_to
        prev_to.next = new_node
        
        # If there was a node after prev_to, update its prev pointer
        if new_node.next:
            new_node.next.prev = new_node
        # If prev_to was the tail, update _tail
        else: 
            self._tail = new_node
            
        self._size += 1
        
    def insert(self, data, next_to):
        current = self._front
        
        # Compares the current is not empty (the end of the list) and current.data is not next
        while current and current.data != next_to:
            current = current.next
            
        # if value not found, raise error
        if current is None:
            raise ValueError(f"Positional element {next_to} is not in the list")
        
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        
        # Update the next node's prev pointer if it exists
        if new_node.next:
            new_node.next.prev = new_node    
        # If inserted at the end, update tail
        else:
            self._tail = new_node
            
        self._size += 1
        
    def delete(self, data):
        current = self._front
        
        while current:
            # If the front/current is data
            if current.data == data:
                # Update previous node
                if current.prev:
                    current.prev.next = current.next
                # Deleting head
                else:
                    self._front = current.next

                # Update next node
                if current.next:
                    current.next.prev = current.prev
                # Deleting tail
                else:
                    self._tail = current.prev

                self._size -= 1
                return True
            # if fornt/current is not data, continue searching
            else: 
                current = current.next

        return False
    
    def search(self, data):
        current = self._front
        
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        
        return False