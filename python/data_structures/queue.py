from data_structures.invalid_operation_error import InvalidOperationError
class Node:
    """
    creates new Node
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Creates Queue class
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        #check to see if queue is empty
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
       if self.front is None:
           raise InvalidOperationError("Stack is empty")
       dequeued = self.front
       self.front = self.front.next
       return dequeued.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        peeked = self.front
        return peeked.value

    def is_empty(self):
        if self.front is None:
            return True
