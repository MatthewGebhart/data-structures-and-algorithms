
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Put docstring here
    """
    def __init__(self):
        self.root = None

    def post_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in post order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.post_order(root.left, nodes)
        # Right Child
        if root.right:
            self.post_order(root.right, nodes)
        # Root
        nodes.append(root.value)

        # print(f"the state of nodes is {nodes}")
        #Base Case
        return nodes


    def pre_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in pre order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Root
        nodes.append(root.value)
        # Left child
        if root.left:
            self.pre_order(root.left, nodes)
        # Right Child
        if root.right:
            self.pre_order(root.right, nodes)

        # print(f"the state of nodes is {nodes}")
        # Base Case
        return nodes

    def in_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in in order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.in_order(root.left, nodes)
        # Root
        nodes.append(root.value)
        # Right Child
        if root.right:
            self.in_order(root.right, nodes)

        # print(f"the state of nodes is {nodes}")
        # Base Case
        return nodes


    def find_maximum_value(self):
        if self.root is None:
            return None
        all_nodes = self.post_order()
        max_val = 0
        for num in all_nodes:
            if num > max_val:
                max_val = num
        return max_val








# if __name__ == "__main__":
#     """
#          1
#         / \
#        2  3
#       / \ / \
#      4  5 6  7
#     """
#     bt_1 = BinaryTree()
#     bt_1.root = Node(1)
#     bt_1.root.left = Node(2)
#     bt_1.root.right = Node(3)
#     bt_1.root.left.left = Node(4)
#     bt_1.root.left.right = Node(5)
#     bt_1.root.right.left = Node(6)
#     bt_1.root.right.right = Node(7)
#
#
# bt_1.post_order()
