# Challenge 06
New Implementation of a Singly Linked List
file located at ./data_structures/linked_list.py
## Challenge
- Extending an implementation
### Feature Tasks
- Add these methods to the LinkedList class:
  - append
    - arguments: new value
    - adds a new node with the given `value` to the end of the list
  - insert before
    - arguments: value, new value
    - adds a new node with the given new value immediately before the first node that has the value specified
  - insert after
    - arguments: value, new value
    - adds a new node with the given new value immediately after the first node that has the value specified
### Whiteboard
![linked_list_insertions_whiteboard.png](linked_list_insertions_whiteboard.png)
new methods to add to Linked List class

## Approach & Efficiency
- Made a Linked List Class to instantiate a new linked list
- added methods for insert, includes and "to string"
- made a Node class to create new nodes
- Big O is O(n) for both space and time because it will depend on how many nodes are present in the list.


## API
LinkedList class now has the following Methods available
- insert `insert(self, value)` will insert a new node to the head of the linked list with the supplied value
- includes `includes(self, value)` will return True if the value provided is included in the linked list
- to string `__str__(self)` returns a string containing the contents of the full linked list.
- append `append(new value` adds a new node with the given `new value` to the end of the list.
- insert before `insert_before(value, new value)`adds a new node with the given new value immediately before the first node that has the value specified
- insert after `insert_after(value, new value)`adds a new node with the given new value immediately after the first node that has the value specified

## Solution

this is a linked - list data structure and can not be run alone, it can be incorporated into other products as a module with the following import
`from data_structures.linked_list import LinkedList`

## Testing
- test to prove the following functionality:
  - Can successfully add a node to the end of the linked list
  - Can successfully add multiple nodes to the end of a linked list
  - Can successfully insert a node before a node located in the middle of a linked list
  - Can successfully insert a node before the first node of a linked list
  - Can successfully insert after a node in the middle of the linked list
  - Can successfully insert a node after the last node of the linked list

all tests are passing

- Tests are accessed in ./tests/code_challenges/test_linked_list_insertions.py
