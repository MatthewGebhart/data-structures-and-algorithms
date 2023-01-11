from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    """
    returns a list of all values in a tree in the order they were encountered
    """
    output_list = []
    queue = Queue()
    queue.enqueue(tree.root)

    if tree.root is None:
        return output_list

    while queue.front:
        current = queue.dequeue()
        output_list.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return output_list
