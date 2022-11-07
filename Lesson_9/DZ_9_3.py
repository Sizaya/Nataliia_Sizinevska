class Parallelogram:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def get_area(self):
        return self.width * self.lenght


class Square(Parallelogram):
    def get_area(self):
        return self.width * self.width


p = Parallelogram(5, 7)
print(p.get_area())
p1 = Square(5, 5)
print(p1.get_area())