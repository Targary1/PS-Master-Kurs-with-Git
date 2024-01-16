import math


# Klassenattribute !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Person:
    counter = 0  # Klassenattribut

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.counter += 1

    def print_details(self):
        print(f'{self.first_name} {self.last_name} ist {self.age} Jahre alt')


#  Statische Methoden mit function decorator  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Math:
    @staticmethod  # Methode aufrufbar ohne vorher eine Instanz der Klasse definieren zu müssen
    def multiply(a, b):
        return a * b


class Circle1:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    @staticmethod  # gehört der Klasse Circle an, aber man will Methode aufrufen ohne ein Objekt vorher instanziiert gehabt zu haben.
    def convert_area_in_radius(area):
        return math.sqrt(area / math.pi)


# Klassenmethoden !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Circle:
    counter = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.counter += 1

    def area(self):
        return math.pi * self.radius ** 2

    @staticmethod
    def convert_area_in_radius(area):
        return math.sqrt(area / math.pi)

    @classmethod
    def from_area(cls, area):  # Alternativer Konstruktor !!!!!!!!!!!!!
        r = math.sqrt(area / math.pi)
        return cls(r)  # <-- cls sehr wichtig, da so Klassenname direkt mit übergeben wird

    @classmethod
    def print_counter(cls):  # Aufrufbar mit oder ohne Instanz
        print(f'Anzahl der erzeugten Circle Objekte: {cls.counter}')


class Rim(Circle):
    pass


rim = Rim.from_area(20)
print(type(rim))


#  Property Attribute (Getter und Setter Methoden) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Zum Validieren von Änderungen a Properties
class Circle:

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    # def get_radius(self):
    #     return print(f'{self._radius}')
                                             #  Getter- und Setter-Methoden
    # def set_radius(self, radius):
    #     if radius >= 0:
    #         self._radius = radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius



#
# print(c.area())
# c.radius=-10
# print(c.radius)



# Magic Methods __function__ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    # def get_radius(self):
    #     return print(f'{self._radius}')
                                             #  Getter- und Setter-Methoden
    # def set_radius(self, radius):
    #     if radius >= 0:
    #         self._radius = radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius

    def __len__(self):  # Länge eines Kreises neu definieren
        return self._radius

    def __str__(self):  # Ausgabe beim Printen des Objektes
        return "Circle(radius" + str(self._radius) + ")"

    def __call__(self, *args, **kwargs):
        print("Eine Instanz kann auch als Funktion aufgerufen werden ...")

    def __add__(self, x):
        if isinstance(x, Circle):
            return self._radius + x._radius  # Klassenattribut durch Aufruf der Instanz mit x addieren


c = Circle(5)
c2 = Circle(7)
print(len(c))
print(c + c2)
c()

#test