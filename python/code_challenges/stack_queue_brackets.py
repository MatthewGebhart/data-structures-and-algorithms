from data_structures.stack import Stack

# class Node:
#     """
#     creates new Node
#     """
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# Hmm,,, I guess this works without a Node class defined here. The Stack class import must also import that Node class


def multi_bracket_validation(str):
    stack = Stack()
    open_br = ["(", "[", "{"]
    close_br = [")", "]", "}"]
    for x in str:
        if x in open_br:
            stack.push(x)
        if x in close_br:
            if stack.is_empty() or close_br.index(x) != open_br.index(stack.pop()):
                return False
    return True

