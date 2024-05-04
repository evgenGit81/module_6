# -*- coding: utf-8 -*-
class Car:
    """Автомобиль"""
    price = 1000000
    power = 100
    model = "ВАЗ"

    def __init__(self):
        print("Модель авто: ", self.model)
        print("Цена автомобиля: ", self.price)

    def horse_powers(self):
        """Мощность двигателя"""
        print("мощность двигателя: ", self.power)


class Nissan(Car):
    """ модель Nissan """
    price = 2500000
    model = "Nissan"
    def horse_powers(self):
        """Мощность двигателя"""
        print("мощность двигателя: ", 170)


class Kia(Car):
    """ модель Kia """
    price = 2750000
    model = "Kia"
    def horse_powers(self):
        """Мощность двигателя"""
        print("мощность двигателя: ", 132)


cars = Car()
cars.horse_powers()
nissik = Nissan()
nissik.horse_powers()
kiak = Kia()
kiak.horse_powers()
