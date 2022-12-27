class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
    def includes(self, target_value):
        start = self.head
        while start is not None:
            if start.value == target_value:
                return True
            start = start.next
        return False
    def __str__(self):

        current = self.head
        return_string = ""

        while current:
            return_string += f"{{ {current.value} }} -> "
            current = current.next
        return_string += "NULL"
        return return_string





class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # def __repr__(self):
    #     return f'<Node(val={self.val}, next={self.next})>'

class TargetError:
    pass



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(4)
    linked_list.insert(7)
    print(linked_list.includes(4))
    print(linked_list.__str__())
    print(linked_list)
