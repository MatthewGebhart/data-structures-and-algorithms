from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    clone_tree = tree.clone()
    def fizz_buzzify(root):
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "FizzBuzz"
        elif root.value % 3 == 0:
            root.value = "Fizz"
        elif root.value % 5 == 0:
            root.value = "Buzz"
        else:
            root.value = str(root.value)
        for n in root.children:
            fizz_buzzify(n)


    fizz_buzzify(clone_tree.root)
    return clone_tree

