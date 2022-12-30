from data_structures.linked_list import LinkedList
def zip_lists(a, b):
    new_list = LinkedList()
    a_current = a.head
    b_current = b.head

    while a_current or b_current:
        if a_current:
            new_list.append(a_current.value)
            a_current = a_current.next
        if b_current:
            new_list.append(b_current.value)
            b_current = b_current.next
    return new_list
