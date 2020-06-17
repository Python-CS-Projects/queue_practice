class BST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Methods
    def insert(self, newValue):
        if self.value < newValue:  # If true go Rigth
            if self.right is None:  # If rigth is empty
                self.right = BST(newValue)  # Add  the new value node
            else:  # If not empty recurse
                self.right.insert(newValue)  # Recursion
        elif newValue < self.value:  # If true go Left
            if self.left is None:
                self.left = BST(newValue)  # Add  the new value node
            else:  # If not empty recurse
                self.left.insert(newValue)  # Recursion
        # At the end the stack starts returning all the recursive calls

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


bts = BST(10)  # Parameter = Root
bts.insert(5)
bts.insert(2)
bts.insert(7)
