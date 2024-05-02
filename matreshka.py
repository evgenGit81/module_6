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
    power = 170
    model = "Nissan"


class Kia(Car):
    """ модель Kia """
    price = 2750000
    power = 135
    model = "Kia"


nissik = Nissan()
nissik.horse_powers()
kiak = Kia()
kiak.horse_powers()
