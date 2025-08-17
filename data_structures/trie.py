from node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        # Travel through each character
        for char in word:
            # If the character is not in the children, create node with the character
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char] # Move current to the child
        
        # Mark last node as the end of a word
        current.is_end_of_word = True
        
    def search(self, word):
        current = self.root
        
        # Travel through each character
        for char in word:
            # If the character is not in the children, return False
            if char not in current.children:
                return False
            current = current.children[char] # Move current to the child
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        current = self.root
        
        # Travel through each character in the prefix
        for char in prefix:
            # If the character is not in the children, return False
            if char not in current.children:
                return False
            current = current.children[char] # Move current to the child
        return True
    
    def delete(self, word):
        
        # Recursive helper
        def _delete(node, word, depth):
            # When we haven't reached the end of the word
            if depth == len(word):
                # If the node is not the end pof the world, return false
                if not node.is_end_of_word:
                    return False
                # If not, unmark the end of the word and there're no children
                node.is_end_of_word = False
                return len(node.children) == 0
            
            # Character at the current position in the word
            char = word[depth]
            
            # If the character is not in the children, return false
            if char not in node.children:
                return False
            
            # If it is, recurse to the next character
            should_delete_child = _delete(node.children[char], word, depth + 1)
            
            # If we got a possible deletion
            if should_delete_child:
                # Remove the children from the current node 
                del node.children[char]
                # Return true if no children and not the end of the word
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        # Recursion init from the root
        _delete(self.root, word, 0)
            
            