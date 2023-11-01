class Pet():

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def say(self):
        print("РРР")


class Cat(Pet):

    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Мяу")


class Fox(Pet):

    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Фыр-фыр")


class Hybrid(Cat, Fox):

    def __init__(self, name):
        super().__init__(name)


pet = Pet("Rex")
print("Instance of class Pet was created with name Rex. It says:")
pet.say()

fox = Fox("Alice")
print("Instance of class Fox was created with name Alice:")
fox.say()

cat = Cat("Roxy")
print("Instance of class Cat was created with name Roxy:")
cat.say()

hybrid = Hybrid("Tucker")
print("Instance of class Hybrid was created with name Tucker (it says what it's first parent - Cat - says):")
hybrid.say()
