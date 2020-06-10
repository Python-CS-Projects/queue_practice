import doubly_linkedlist as Dll

'''
FILO: First in last out
'''


class Stack:
    def __init__(self):
        self.len = 0
        self.list = Dll.DoublyLinkedList()

    def push(self, value):
        self.list.add_to_head(value)
        self.len += 1

    def pop(self):
        self.list.remove_from_head()
        if self.len > 0:
            self.len -= 1

    def get_len(self):
        print(self.len)

    def get_values(self):
        self.list.get_values()


# stack = Stack()

# stack.push(10)
# stack.push(2)
# stack.push(3)
# stack.push(130)
# stack.get_values()
# stack.pop()
# stack.pop()
# stack.get_values()
# stack.get_len()
