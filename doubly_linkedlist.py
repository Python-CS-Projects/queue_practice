'''
Implementing a Doubly LL to use on the Queue and stack practices
'''


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # Optional helper methods below
    def insert_after(self, value):  # Method for each node to add after it self
        curr_next = self.next  # get the current next for itself if is the tail is None
        self.next = Node(value, self, curr_next)  # Create a new node 1-2-3
        if curr_next:  # if a current next exist
            curr_next.prev = self.next  # set the prev as the new Node created above

    def insert_before(self, value):
        self.prev = value

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    # Helper methods below
    def add_to_head(self, value):
        new_node = Node(value)  # create a new node from the provided value
        if self.head is None:  # if LL is empty
            self.head = new_node
            self.tail = new_node
        else:  # if there is only one item in the LL
            new_node.next = self.head  # set the curr head as the next val of the new node
            self.head.prev = new_node  # set new node as prev of curr head
            self.head = new_node  # Set new node as new head

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.length > 0:  # if NOT empty
            # make the new node the new next of curr tail
            self.tail.insert_after(value)
            # set the tail as the curr tail new next which is the new value
            self.tail = self.tail.next
            self.length += 1
        elif self.length == 0:  # if empty
            self.head = new_node
            self.tail = new_node
            self.length += 1

    def get_values(self):
        curre_node = self.head
        arr = []
        while curre_node.next is not None:
            print(curre_node.value)
            arr.append(curre_node.value)
            curre_node = curre_node.next
        print(arr)


list = DoublyLinkedList()

list.add_to_tail(29)
list.add_to_tail(88)
list.get_values()
