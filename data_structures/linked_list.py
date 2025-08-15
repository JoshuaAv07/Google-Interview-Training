from node import ListNode as Node
from structure import Structure

class LinkedList(Structure):
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
            self._tail = node
            
        self._size +=1
        
    def insertAfter(self, data, prev_to):
        # Make sure the previous exists
        if prev_to == None:
            print("Cannot be NULL")
            return

        new_node = Node(data)
        new_node.next = prev_to.next
        prev_to.next = new_node

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
        current.next = new_node
        
        # Update tail if the insertion was at the end
        if current == self._tail:
            self._tail = new_node
            
        self._size += 1
        
    def delete(self, data):
        # Empty List
        if self._front == None:
            return False
        
        # Deleting the head
        if self._front.data == data:
            self._front = self._front.next
            self._size -= 1
            # If the list becomes empty
            if self._front == None:
                self._tail = None
            return True

        # Deleting from the middle or end
        current = self._front
        
        while current.next:
            if current.next.data == data:
                # Deleting the tail
                if current.next == self._tail:
                    current.next = None
                    self._tail = current
                # Deleting from the middle
                else: 
                    current.next = current.next.next
                
                self._size -=1
                return True
            # Continue until finding it
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