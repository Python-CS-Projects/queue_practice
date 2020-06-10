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
        curr_next = self.next  # save curr next before we change it to new value
        # Create a new node with reference to prev as current value and next as the next of the curr value
        self.next = Node(value, self, curr_next)
        if curr_next:  # if a current next exist
            curr_next.prev = self.next  # set the prev as the new Node created above

    def insert_before(self, value):
        curr_prev = self.prev  # save curr prev
        self.prev = Node(value, curr_prev, self)  # set prev as new node
        if curr_prev:  # if a curr exist meaning is not None
            curr_prev.next = self.prev  # set curr prev next as the new node

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
        if self.length > 0:  # Not empty LL
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        elif self.length == 0:  # Empty LL
            self.head = new_node  # Set new node as new head
            self.tail = new_node
            self.length += 1

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

    def remove_from_head(self):
        if self.head is None:  # If empty
            print("Error, cannot remove from an empty list.")
            return
        elif self.head is self.tail:  # if only one item
            self.head = None
            self.tail = None
            self.length = 0  # set to empty because we remove the only item
        else:  # if more than one item
            new_head = self.head.next  # save item after head as new head
            new_head.prev = None  # set the prev of new head as None
            self.head = new_head  # finally set new head
            self.length -= 1

    def remove_from_tail(self):
        if self.tail is None:  # If empty
            print("Error, cannot remove from an empty list.")
            return
        elif self.head is self.tail:  # if only one item
            self.head = None  # set to none
            self.tail = None  # set to none
            self.length = 0  # set to empty because we remove the only item
        else:  # if more than one item
            new_tail = self.tail.prev  # save the prev of current tail
            new_tail.next = None  # set the next of new tail as none
            self.tail = new_tail  # finaly save the new tail as the tail
            self.length -= 1

    def delete(self, value):
        if self.tail is None:  # If empty
            print("Error, cannot remove from an empty list.")
            return
        elif self.head.value == value:
            self.remove_from_head()
        elif self.tail.value == value:
            self.remove_from_tail()
        else:
            curr_node = self.head
            while curr_node is not None:
                if curr_node.value == value:
                    prev_node = curr_node.prev
                    next_node = curr_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    self.length -= 1
                    return
                curr_node = curr_node.next
            print(f"{value} not found")

    def get_values(self):
        curre_node = self.head
        arr = []
        if self.head is None:
            print("Empty list.")
            return
        while curre_node is not None:
            arr.append(curre_node.value)
            curre_node = curre_node.next
        print(arr)
        print(f"Currenty {self.length} items in the LL")


list = DoublyLinkedList()

list.add_to_head(34)
list.add_to_head(37)
list.add_to_tail(29)
list.add_to_tail(88)
list.get_values()
list.delete(9)
list.get_values()
# list.remove_from_head()
# list.remove_from_tail()
# list.get_values()
