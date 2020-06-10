import doubly_linkedlist as Dll

'''
FIFO: First in first out
'''


class Queue:
    def __init__(self):
        self.len = 0
        self.list = Dll.DoublyLinkedList()

    def enqueue(self, value):  # Add to the back of the line
        self.list.add_to_tail(value)  # add to the end of the line
        self.len += 1

    def dequeue(self):  # Remove from the front of the line
        self.list.remove_from_head()
        if self.len > 0:
            self.len -= 1

    def get_len(self):
        print(f"Currently {self.len} items in the queue.")

    def getValues(self):
        self.list.get_values()


# x = Queue()
# x.enqueue(1)
# x.enqueue(2)
# x.enqueue(3)
# x.dequeue()
# x.get_len()
# x.getValues()
