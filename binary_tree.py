class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Methods
    def insert(self, value):
        pass

    def contains(self, target):  # Recursive
        if self.value == target:
            return True
        elif self.value < target:
            if not self.left:
                return False
            self.left.contains(target)
        else:
            if not self.right:
                return False
            self.right.contains(target)

    def get_max(self):
        pass

    def for_each(self):
        pass


bts = BST(10)  # Parameter = Root

bts.insert(5)
bts.insert(2)
bts.insert(7)
