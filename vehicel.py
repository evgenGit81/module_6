# -*- coding: utf-8 -*-
class Vehicel:
    def get_type(self):
        return self.__vehicel_type
    def set_type(self, vehicel_type="none"):
        self.__vehicel_type = vehicel_type
    def del_type(self):
        del self.__vehicel_type
    v_type = property(fget=get_type, fset=set_type, fdel=del_type, doc="Тип транспортного средства")


class Car:
    price = 1000000
    def horse_power(self, power=100):
        return f"Мощность двигателя автомобиля: {power}"


class Nissan(Vehicel, Car):
    vehicel_type = "Седан-универсал"
    price = 2300000
    def horse_power(self):
        return f"Мощность двигателя автомобиля: 200 л.с."


car = Nissan()
print(car.vehicel_type)
print(car.horse_power())
print(car.price)
ccar = Car()
print(ccar.price, ccar.horse_power())
fcar = Vehicel()
fcar.v_type = "Седан"
print(fcar.v_type)


