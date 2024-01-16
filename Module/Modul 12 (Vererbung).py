import math


# Inheritance good for less redundance, reusage, adding later on attributes easily !!!!!!!!!!!!!!!!!

class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Ich schlafe gerade...")

    def move_fast(self):
        print("Aktuelle Geschwindigkeit 20 kmh")


class Dog(Animal):

    def bark(self):
        print("Wau Wau")


class Cat(Animal):

    def purr(self):
        print("Schnur Schnur")


class Tiger(Animal):
    def move_fast(self):
        print("Aktuelle Geschwindigkeit 20 kmh")


class Owl(Animal):

    def __init__(self, name, age, color, fav_food, hunting_instinct):
        super().__init__(name, age, color, fav_food)
        self.hunting_instinct = hunting_instinct

    def sleep(self):
        super().sleep()  # self Attribut nimmt super funktion automatisch
        print("Gleichgewicht halten")


# Name Mangling !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Variablen mit vorangestelltem Underscore _ nur für internen gebrauch innerhalb der
        # Klasse, kann trz darauf zugegriffen werden
        # Variablen mit doppelt vorangestelltem Underscore __ nur für internen gebrauch innerhalb der Klasse, kann
        # nicht mehr darauf zugegriffen werden nur mit _classname__attributename
    def area(self):
        return math.pi * self.__radius ** 2.0


class Rim(Circle):
    def test(self):
        self.__radius = 100


r = Rim(10)
r.test()
print(r._Circle__radius)
print(r._Rim__radius)


#  Mehrfachvererbung !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_details(self):
        print(f'{self.first_name} {self.last_name} ist {self.age} Jahre alt')


class Employee:
    def __init__(self, last_name, id):
        self.last_name = last_name
        self.id = id

    def print_details(self):
        print(f'Mitarbeiter {self.last_name} hat ID-Nummer {self.id}')

class Teacher(Person, Employee):  # Reihenfolge links nach rechts beim Abfragen (Method Resolution Order MRO)
    def __init__(self, first_name, last_name, age , id):
        Person.__init__(self, first_name, last_name, age)
        Employee.__init__(self, last_name, id)

teacher_1 = Teacher("Max", "Mustermann", 31, 2)
teacher_1.print_details()

employee_1 = Employee("Schmidt", 567)
employee_1.print_details()

person_1 = Person("Jürgen", "Klopp", 18)
person_1.print_details()


#test