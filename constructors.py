class Point:
    def __init__(self,x,y):
      self.x = x
      self.y = y
    def move():
        print(point1.x)
     
        print("Move")

    def draw(self):
        print("Draw")


#An object is an instance of the class
point1 = Point(10,20)

print(point1.x,point1.y)

##Exercise

class Person:
    def __init__(self, name):
        self.name = name

    def name3(self):
            name2 = input("Enter your name:  ")
            print(name2)


    def talk(self):
            print(f"Boy can yo talk? {self.name} ")



Roshan = Person('RoshanRon')
print(Roshan.name)

Roshan1 = Person('x')
Roshan1.name3()
Roshan.talk()
Roshan1.talk()