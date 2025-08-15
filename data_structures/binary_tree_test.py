from binary_tree import BinaryTree

if __name__ == '__main__':

    bst = BinaryTree()
    print(" INSERT DATA ".center(50, '-'))
    print(bst.insert(10))
    print(bst.insert(8))
    print(bst.insert(12))
    print(bst.insert(5))
    print(bst.insert(9))
    print(bst.insert(11))
    print(bst.insert(15))
    print(bst.insert(3))
    print(" DATA SIZE ".center(50, '-'))
    print(bst.size())
    
    print(" INORDER ".center(50, '-'))
    bst.inorder(bst.root())
    print()
    print(" PREORDER ".center(50, '-'))
    bst.preorder(bst.root())
    print()
    print(" POSTORDER ".center(50, '-'))
    bst.postorder(bst.root())
    print()

    print(" SEARCH 1 ".center(50, '-'))
    node = bst.search(bst.root(), 4)
    print(node.data if node else "Not found")
    print()

    print(" SEARCH 2 ".center(50, '-'))
    node = bst.search(bst.root(), 3)
    print(node.data if node else "Not found")
    print()

    print(" SEARCH 3 ".center(50, '-'))
    node = bst.search(bst.root(), 12)
    print(node.data if node else "Not found")
    print()

    bst.delete(bst.root(), 10)
    print(" INORDER ".center(50, '-'))
    bst.inorder(bst.root())