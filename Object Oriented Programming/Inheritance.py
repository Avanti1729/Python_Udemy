class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")


my_animal = Animal()
my_animal.who_am_I()
my_animal.eat()


# Creating an Inherited Class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_I(self):
        print("I am a dog")

    def Bark(self, num):
        print("WOOF! I am {} dog".format(num))


my_dog = Dog()
my_dog.eat()
my_dog.who_am_I()
my_dog.Bark(23)


# Class LINE
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((y2 - y1) / (x2 - x1))


line = Line((10, 2), (30, 4))
print(line.distance())


# Class CYLINDER
class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2


cyli = Cylinder(2, 3)
print(cyli.volume())


# Class ACCOUNTS
class Accounts():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep
        print("Deposit Accepted")

    def withdraw(self, withd):
        if self.balance >=withd:
            print(self.balance)
            print("Withdrawal Accepted")
            self.balance -=withd
            print(self.balance)
        else :
            print("Inelligible")
acc=Accounts("Avanti",100)
acc.deposit(40)
acc.withdraw(140)

