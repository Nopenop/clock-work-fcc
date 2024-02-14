class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    def set_width(self, width:float) -> None:
        self.width = width
    def set_height(self, height:float) -> None:
        self.height = height
    def get_area(self) ->float:
        return self.width * self.height
    def get_perimeter(self) -> float:
        return 2*self.width + 2*self.height
    def get_picture(self) ->str:
        ret_str = ""
        for i in range(self.height):
            for j in range(self.width):
                ret_str += "*"
            ret_str += "\n"
        return ret_str
    def get_amount_inside(self, other_rectangle) -> int:
        return self.get_area() // other_rectangle.get_area()
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'



class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f'Rectangle(side={self.width})'
    def set_height(self, height: float) -> None:
        super().set_height(height)
        super().set_width(height)
    def set_width(self, width: float) -> None:
        super().set_height(width)
        super().set_width(width)

r = Rectangle(5, 10)
print(r.get_picture())
s = Square(5)
print(s.get_area())
