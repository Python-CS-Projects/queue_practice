import doubly_linkedlist


class Queue:
    def __init__(self):
        self.len = 0
        self.list = doubly_linkedlist.DoublyLinkedList()

    def enqueue(self, value):
        self.list.add_to_tail(value)  # add to the end of the line
        self.len += 1

    def dequeue(self, value):
        self.list.remove_from_head()

        if self.len > 0:
            self.len -= 1

    def getValues(self):
        self.getValues()


x = Queue()
x.enqueue(4)
x.getValues()
x.dequeue(4)
