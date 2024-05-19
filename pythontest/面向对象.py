# class Car:
#     def infor(self):
#         print("yes car")
#
# car=Car()
# car.infor()
# isinstance(car,Car)
#
# def demo():
#     pass
# if 5>3:
#     pass

class Car:
    price=10000
    def _init_(self,c):
        self.color=c
car1=Car("red")
car2=Car("blue")
print(car1.color,Car.price)
Car.price=1000000
Car.name='QQ'
car1.color="yellow"
print(car2.color,Car.price,Car.name)
print(car1.color,Car.price,Car.name)

import types
def setSpped(self,s):
    self.speed=s
car1.setSpeed=types.MethodType(setSpeed,car1)
