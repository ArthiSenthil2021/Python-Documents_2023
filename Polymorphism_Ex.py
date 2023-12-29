class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def __init__(self, brand, model):
   self.brand1 = brand
   self.model1 = model
   Vehicle.__init__(self,brand,model)

  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def __init__(self, brand, model):
   self.brand1 = brand
   self.model1 = model
   Vehicle.__init__(self,brand,model)

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in [boat1,plane1]:
  print(x.brand)
  print(x.model)
  print(x.model1)
  x.move()
