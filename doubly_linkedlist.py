'''
Implementing a Doubly LL to use on the Queue and stack practices
'''


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # Helper methods below


class DoublyLinkedList:
    def __init__(self,node=None):
        self.head = node
        self.tail = node
        self.count = 1 if node is not None else 0

    #Helper methods below
