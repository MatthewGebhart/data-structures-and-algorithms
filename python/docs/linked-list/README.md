# Singly Linked List
New Implementation of a Singly Linked List
file located at ./data_structures/linked_list.py
## Challenge
### Node Class
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
### Linked List Class
- Create a Linked List class
- Within your Linked List class, include a head property.
  - Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
  - insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
  - includes
    - Arguments: value
    - Returns: Boolean
      - Indicates whether that value exists as a Node’s value somewhere within the list.
  - to string
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:
    - `"{ a } -> { b } -> { c } -> NULL"`

## Approach & Efficiency
- Made a Linked List Class to instantiate a new linked list
- added methods for insert, includes and "to string"
- made a Node class to create new nodes

## API
LinkedList class has the following Methods available
- insert `insert(self, value)` will insert a new node to the head of the linked list with the supplied value
- includes `includes(self, value)` will return True if the value provided is included in the linked list
- to string `__str__(self)` returns a string containing the contents of the full linked list.


## Testing
- Wrote tests to prove the following functionality:
  - Can successfully instantiate an empty linked list
  - Can properly insert into the linked list
  - The head property will properly point to the first node in the linked list
  - Can properly insert multiple nodes into the linked list
  - Will return true when finding a value within the linked list that exists
  - Will return false when searching for a value in the linked list that does not exist
  - Can properly return a collection of all the values that exist in the linked list

- Tests are accessed in ./tests/data_structures/test_linked_list.py
