class Car:
    def __init__(self, brand, color, v_engine):
        self.brand = brand
        self.color = color
        self.v_engine = v_engine

    def drive_forward(self):
        print("Їхати вперед")

    def ride_back(self):
        print("Їхати назад")


class Car2(Car):

    def turn_right(self):
        print("Поворот праворуч")

    def turn_left(self):
        print("Поворот ліворуч")



car = Car2("Honda", "black", 2.0)
car.drive_forward()
car.ride_back()
car.turn_right()
car.turn_left()