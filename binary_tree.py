class BST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Methods
    def insert(self, value):
        if self.value < value:  # Go right
            if self.right is None:
                self.right = BST(value)  # Add  the new value node
        elif self.value > value:
            pass

    def contains(self, target):  # Recursive
        if self.value == target:  # Base case
            return True
        elif self.value < target:
            if not self.left:  # If left equals None
                return False  # Not found
            self.left.contains(target)  # Run contains on Left Value
        else:
            if not self.right:  # If right equals None
                return False  # Not found
            self.right.contains(target)  # Run contains on Right Value

    def get_max(self):
        pass

    def for_each(self):
        pass


bts = BST()  # Parameter = Root
bts.insert(5)
bts.insert(2)
bts.insert(7)
