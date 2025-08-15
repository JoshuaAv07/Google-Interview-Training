from node import BinaryTreeNode as Node

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, data):
        node = Node(data) 
        
        # Creates root if empty
        if not self._root:
            self._root = node
            self._size += 1
            return node.data
        
        current = self._root
        
        while True:
            # If the value is smaller than the current node go left
            if data < current.data:
                # If left child, continue down left and repeat
                if current.left:
                    current = current.left
                # If no left child, insert the new node and break loop
                else:
                    current.left = node
                    break
            # If the value is not smalle than the current node go right
            else:
                # If right child, continue down right and repeat
                if current.right:
                    current = current.right
                # If no right child, insert the new node and break loop
                else:
                    current.right = node
                    break
                    
        self._size += 1
        return node.data
            
    # Shows all numbers from the lower to the highest (including the main root)
    def inorder(self, current): 
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)

    # Shows the main root number an the the rest numbers from the lower to the highest
    def preorder(self, current): 
        if current:
            print(current.data, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    # First shows the numbers from the lower to the highest and at the end goes the main root
    def postorder(self, current): 
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=' ')

    # If root exists or not
    def root(self):
        if self._root:
            return self._root
        else:
            return None
        
    def size(self): 
        return self._size

    # The leaf with the minimum value
    def min(self, current):
        # Stop when there’s no more left child
        while current and current.left:
            current = current.left
        return current  

    # The leaf with the maximum value
    def max(self, current):
        # Stop when there’s no more right child
        while current and current.right:
            current = current.right
        return current
    
    def search(self, current, data):
        # Return the node if it's None or matches the search value
        if current is None or current.data == data:
            return current

        # If data is smaller than the current node go left
        if data < current.data:
            return self.search(current.left, data)
        # If data is not smaller than the current node go right
        elif data > current.data:
            return self.search(current.right, data)

    def delete(self, current, data):
        # If empty
        if current is None:
            return current

        # If the value is smaller than the current value search left
        if data < current.data:
            current.left = self.delete(current.left, data)
        # If the value is greater than the current value search right
        elif data > current.data:
            current.right = self.delete(current.right, data)
        # Node found 
        else:
            # If current node has no left return right
            if current.left is None:
                return current.right
            # If current node has no right return left
            elif current.right is None:
                return current.left
            
            # If two children (delete right, succesor, it is right just by book convention)
            # Find smallest in right subtree, need to save the current because if we remove we break the tree
            temp = self.min(current.right)
            current.data = temp.data
            # Delete the smallest in right subtree
            current.right = self.delete(current.right, temp.data)

        return current