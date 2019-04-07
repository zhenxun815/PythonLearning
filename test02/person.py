class Person:
    # Class variables,only one copy, all instances share
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}".format(self.name))
        Person.population += 1

    def die(self):
        print("{} is going to die!".format(self.name))

        Person.population -= 1
        if Person.population == 0:
            print("{} was the last one...".format(self.name))
        else:
            print("There are still {:d} living person.".format(Person.population))

    def say_hi(self):
        print('hello,name is:', self.name)

    @classmethod
    def how_many(cls):
        print("Person population is {:d}".format(cls.population))


p1 = Person('Yiheng')
p1.say_hi()
Person.how_many()

p2 = Person('test')
p2.say_hi()
Person.how_many()

print('kill test')
p2.die()
Person.how_many()
