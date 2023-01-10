from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
 Subclass of BinaryTree
    """
    def add(self, value):
        """
        Following the rules of a BST, adds the value to the tree in the correct location
        """
        # check for empty BST
        if self.root is None:
            self.root = Node(value)
            return

        # start pointer at root
        current = self.root

        while current:
            # if value == current.value:
            #     return print("node already exists")

            # if number of the added node is less than current node, check left
            if value < current.value:
                # add node only if there's space
                if current.left is None:
                    current.left = Node(value)
                    return

                # if there is no space, go left
                current = current.left

            # if number of the added number is greater than current node, go right
            else:
                # add node only if there is space
                if current.right is None:
                    current.right = Node(value)
                    return

                current = current.right

    def contains(self, target):
        """
        searches through the BST looking for target and returns TRUE if it is present
        """
        # start pointer at root
        current = self.root

        while current:
            #check if root is target
            if target == current.value:
                return True

            if target < current.value:
                current = current.left

            if target > current.value:
                current = current.right

        return False

