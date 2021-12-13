class Mammals:
    def walk(self):
        print("walk")


class Dog(Mammals):
    def bark(self):
        print("Bark")
 


class Cat(Dog):
    def meow(self):
        print("Meow")


A = Dog()
A.walk()
A.bark()

B = Cat()
B.walk()
B.meow()



