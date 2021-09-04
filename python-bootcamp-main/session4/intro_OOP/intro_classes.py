# source: https://www.csdojo.io/class

class Robot: #module
    #Initilize key vars using constructor
    def __init__(self, name, color, weight): #methods with main components such as name color weight
        self.name = name
        self.color = color
        self.weight = weight
        self.height = 10

    def introduce_self(self):
        print("My name is " + self.name)

    def calc_area(self):
        area = self.weight * self.height


    def set_properties(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.height = 10

#r1 = Robot() #robot class wont walk, but once you initialize, robot must have sth in ()
# r1.name = "Tom" #accessing vars from constructor
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()
r2.set_properties("Megan", "red", 9, 19)
total = r2.calc_area() + r1.calc_area()