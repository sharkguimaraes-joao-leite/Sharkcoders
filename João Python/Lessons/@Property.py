#@property = Decorator used to define methods as a property

class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # The underscore makes the variables private (shouldn't be changed/used externally)

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("The width must be greater than 0")
            print("---------------------------")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("The height must be greater than 0")
            print("---------------------------")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle1 = rectangle(6, 4)

rectangle1.width = 0
rectangle1.height = 4

print(rectangle1.width)
print(rectangle1.height)
print("---------------------------")

del rectangle1.width
del rectangle1.height