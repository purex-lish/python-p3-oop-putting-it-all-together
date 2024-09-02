# # #!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize private variable for size
        self.size = size  # Use the setter to validate and set size
        self.condition = 'New'  # Default condition for a new shoe

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            # no exception raised if you want to pass the test checking for printed output
            return
        self._size = value

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
