"""
Домашка,
доделываем классы с занятия,

Сложность 1)
Добавить класс VIPProduct наследованный от Product,
на него скидка не расспростаняется

Сложность 2)
Сделать возможность задавать скидку при инициализации продукта (Если не задана, оставить 20%)

Сложность 3)
a) Добавить информацию о кол-ве продуктов на складе,
b) добавить покупателям метод купить продукт(или несколько),
c) при покупке у клиента должен уменьшатся бюджет,
d) а у продукта уменьшать кол-во на складе

Сложность 4)
a) Дописать возможность добавлять продукты на склад,
b) и пополнять бюджет клиента
"""

from math import trunc


class WhereIsMoney(Exception):
    pass


class WhatProduct(Exception):
    pass


class Product:
    def __init__(self, name: str, price: float, in_stock: int = 10, discount: float = 0.8):
        self.name = name
        self.price = price
        self.discount = discount  # Сложность 2) Сделать возможность задавать скидку при инициализации продукта
        self.in_stock = in_stock  # Сложность 3. a) Добавить информацию о кол-ве продуктов на складе


class VipProduct(Product):
    """ Сложность 1) Добавить класс VIPProduct наследованный от Product,
        на него скидка не расспростаняется """

    def __init__(self, name: str, price: float, in_stock: int = 10, discount: float = 1):
        super().__init__(name=name, price=price, in_stock=in_stock, discount=discount)


class Buyer:
    """ обычный покупатель без скидки """

    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = self.check_budget(budget)

    def get_quantity_of_product(self, product: Product):
        """ сколько единиц одного продукта может купить покупатель """
        self.check_product(product)
        return trunc(self.budget / product.price)

    @staticmethod
    def check_product(product):
        """ проверка существования продукта"""
        if not isinstance(product, Product):
            raise WhatProduct('нет такого продукта?')

    @staticmethod
    def check_budget(budget):
        """ проверяет что у пользователя в кошельке, если не число возвращает 0 """
        valid_type = (int, float)
        if type(budget) == str:
            budget = float(budget) if budget.isdigit() else 0
        if type(budget) in valid_type and budget < 0:
            budget = 0
        return budget


class VipBuyer(Buyer):
    """ Vip покупатель скидка 20% """

    def __init__(self, name, budget: float):
        super().__init__(name=name, budget=budget)

    def get_quantity_of_product(self, product: Product):
        return trunc(super().get_quantity_of_product(product) / product.discount)


class SuperVipBuyer(VipBuyer):
    """ SuperVip покупатель скидка 36% """

    def __init__(self, name: str, budget: float):
        super().__init__(name=name, budget=budget)

    def get_quantity_of_product(self, product: Product):
        return trunc(super().get_quantity_of_product(product) / product.discount)


if __name__ == "__main__":
    bread = Product(name='Bread', price=20, in_stock=200, discount=0.8)
    wine = Product(name='Wine', price=60, in_stock=200, discount=0.8)
    grecha = VipProduct(name='Grecha', price=10, in_stock=100)

    usr = Buyer(name="Petro", budget=200)
    vip_usr = VipBuyer(name="Pavlo", budget=200)
    super_vip_user = SuperVipBuyer(name="Stepan", budget=200)

    print(usr.get_quantity_of_product(product=bread))
    print(vip_usr.get_quantity_of_product(product=bread))
    print(super_vip_user.get_quantity_of_product(product=bread))

    print(usr.get_quantity_of_product(product=grecha))
    print(vip_usr.get_quantity_of_product(product=grecha))
    print(super_vip_user.get_quantity_of_product(product=grecha))

    pepper = Product(name='pepper', price=10, in_stock=100)

    print(usr.get_quantity_of_product(product=pepper))
    print(vip_usr.get_quantity_of_product(product=pepper))
    print(super_vip_user.get_quantity_of_product(product=pepper))
