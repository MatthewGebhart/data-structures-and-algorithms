from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    Following the rules of a BST, adds the value to the tree in the correct location
    """

    def __init__(self, value=None):
        super().__init__()
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value == self.value:
            return print("node already exists")
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.add(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

