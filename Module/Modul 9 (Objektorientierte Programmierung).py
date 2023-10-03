class Car:
    def __init__(self, car_brand, color=None, *additional):  # Konstruktor
        self.car_brand = car_brand
        self.color = color
        self.horse_power = additional[0]
        self.doors = additional[1]
        self.xpos = 5
        self.ypos = 5
    def drive(self, x, y):
        self.xpos += x
        self.ypos += y

    def print_position(self):
        print(f'Aktuelle Position des Autos: x= {self.xpos} | y= {self.ypos}')

#  car1 = Car("benz", color="schwarz", horse_power=9, doors=5)
car1 = Car("benz", "rot", 5, 6)
print(car1.car_brand, car1.color, car1.horse_power, car1.doors)


car1.drive(5, 15)
print(car1.xpos, car1.ypos)
car1.print_position()

def test(x, z, y=0):
    summe = x + y +z
    return print(summe)
test(3, 7, 9)
