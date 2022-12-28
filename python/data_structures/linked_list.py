class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        """
        adds a new node with value to the head of the list
        """
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
    def includes(self, target_value):
        """
        Indicates whether target_value exists as a Node’s value somewhere within the list.
        """
        start = self.head
        while start is not None:
            if start.value == target_value:
                return True
            start = start.next
        return False
    def __str__(self):
        """
        Returns: a string representing all the values in the Linked List, formatted as:
    - `"{ a } -> { b } -> { c } -> NULL"`
        """
        current = self.head
        return_string = ""

        while current:
            return_string += f"{{ {current.value} }} -> "
            current = current.next
        return_string += "NULL"
        return return_string

    def append(self, new_value):
        """
        adds a new node with new_value to the end of the Linked List
        """
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(value=new_value)
        current.next = new_node

    def insert_before(self, value, new_value):
        """
        adds a new node with new_value immediately before the first node that has the value specified
        """
        current = self.head
        new_node = Node(value=new_value)

        if self.head is None:
            raise TargetError("Error: The list is empty")

        if current.value == value:
            new_node.next = current
            self.head = new_node

        else:
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            else:
                raise TargetError('Target Value is not in list')

    def insert_after(self, value, new_value):
        """
        adds a new node with new_value immediately after the first node that has the value specified
        """
        current = self.head
        new_node = Node(value=new_value)

        if self.head == None:
            raise TargetError("Error: The list is empty")
        else:
            while current.next:
                if current.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            else:
                raise TargetError('Target Value is not in list')

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    def __init__(self, message):
        self.message = message



# if __name__ == "__main__":
#     linked_list = LinkedList()
#     linked_list.insert(3)
#     linked_list.insert(2)
#     linked_list.insert(4)
#     linked_list.insert(7)
#     print(linked_list.includes(4))
#     print(linked_list.__str__())
#     print(linked_list)
