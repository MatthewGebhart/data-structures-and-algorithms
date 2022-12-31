# Stacks and Queues
New implementation of Stack and Queue classes

## Challenge
Challenge Type: New implementation

## Approach & Efficiency
- created Node Class that has value property as well as a next property that defaults to None
- created Stack class that has a top property
- created Queue class that has front and rear properties
- All methods have a Big O of O(1) for both time and space because they are only looking at a single data point

## API
Stack class methods
- push
    - Arguments: value
    - adds a new node with that value to the `top` of the stack with an O(1) Time performance.
- pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
- peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
- is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.

Queue class methods
- enqueue
    - Arguments: value
    - adds a new node with that value to the `back` of the queue with an O(1) Time performance.
- dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
- peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
- is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty


## Testing

- Passing all supplied tests
