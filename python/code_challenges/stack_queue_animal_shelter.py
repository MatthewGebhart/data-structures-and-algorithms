from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.name == "dog":
            self.dog_queue.enqueue(animal)
        if animal.name == "cat":
            self.cat_queue.enqueue(animal)

    def dequeue(self, preference):
        if preference == "cat":
            if self.cat_queue.front is None:
                raise InvalidOperationError("There are no Cats to adopt sorry")
            else:
                return self.cat_queue.dequeue()
        if preference == "dog":
            if self.dog_queue.front is None:
                raise InvalidOperationError("There are no Dogs to adopt sorry")
            else:
                return self.dog_queue.dequeue()
        else:
            print("sorry we only have cats and dogs")
            return None

class Dog:
    def __init__(self, name="dog"):
       self.name = name
       self.next = next



class Cat:
    def __init__(self, name="cat"):
      self.name = name
      self.next = next


if __name__ == "__main__":
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    print(f" cat queue is {shelter.cat_queue}")
