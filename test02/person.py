class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hello,name is:', self.name)


p = Person('Yiheng')
p.say_hi()
