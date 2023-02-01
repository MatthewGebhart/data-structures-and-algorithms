from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_1, tree_2):
    shared_dict = {}
    if tree_1.root is None or tree_2.root is None:
        return None

    def walk(node1, node2):
        if node1 is None or node2 is None:
            return
        if node1.value == node2.value:
            if node1.value not in shared_dict:
                shared_dict[node1.value] = 1
        walk(node1.left, node2.left)
        walk(node1.right, node2.right)

    walk(tree_1.root, tree_2.root)
    return list(shared_dict.keys())
