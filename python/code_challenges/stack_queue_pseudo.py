from data_structures.stack import Stack, Node


class PseudoQueue:

    def __init__(self):
        stack_1 = Stack()
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear is None:
            self.rear = self.top = Node(value)
            return
        self.rear = Node(value)
    def dequeue(self, value):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        self.rear = Node(value)
