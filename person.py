class Person:
    def __init__(self,name):
        self.name = name


    def talk(self):
        print("talk")


john = Person("john smith")
print(john.name)
john.talk()