class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Methods
    def insert(self, value):
        pass

    def contains(self, target):  # Recursive
        if self.value == target:  # Base
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
