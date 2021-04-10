class AbstractCat:

    def __init__(self):
        self.food = 0
        self.weight = 0

    def eat(self, n):
        self.weight = min(100, self.weight + (n + self.food) // 10)
        self.food = (n + self.food) % 10

    def __str__(self):
        return("{name} ({weight})".format(name=type(self).__name__, weight=self.weight))


class Kitten(AbstractCat):

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def meow(self):
        return("meow...")
    
    def sleep(self):
        return("Snore" * (self.weight // 5))


class Cat(Kitten):

    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return("MEOW...")

    def get_name(self):
        return(self.name)

    def catch_mice(self):
        return("Got it!")
