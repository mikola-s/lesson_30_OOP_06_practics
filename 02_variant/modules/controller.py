"""
Домашка, доделываем классы с занятия,

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
    def __init__(self, product_id: int, name: str, price: float, in_stock: int = 10, discount: float = 0.8):
        self.id = product_id
        self.name = name
        self.price = price
        self.discount = discount  # Сложность 2) Сделать возможность задавать скидку при инициализации продукта
        self.in_stock = in_stock  # Сложность 3. a) Добавить информацию о кол-ве продуктов на складе

    def set_in_stock(self, count):
        """ изменяет количество продуктов на складе """
        # Сложность 3) d) а у продукта уменьшать кол-во на складе
        # Сложность 4) a) Дописать возможность добавлять продукты на склад,
        self.in_stock += count


class VipProduct(Product):
    """ класс продукта  без скидки """

    # Сложность 1) Добавить класс VIPProduct наследованный от Product,
    # на него скидка не расспростаняется

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
        return trunc(self.budget / product.price / self.get_discount(product))

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
        return float(budget)

    def buy(self, product: Product, want_to_buy: int = 1):
        """ покупает нужное количество продуктов"""
        if product.in_stock >= want_to_buy:  # на складе есть
            if self.get_quantity_of_product(product) >= want_to_buy:  # достаточно денег
                total_cost = -product.price * want_to_buy * self.get_discount(product)
                self.set_budget(total_cost)
                product.set_in_stock(-want_to_buy)
                return True
            else:
                print(f'у покупателя {self.name} не хватает денег на покупку {want_to_buy} {product.name}')
                print(f'денег хватит на покупку {self.get_quantity_of_product(product)} {product.name}')
        else:
            print(f'на складе {product.in_stock} {product.name}')
        return False

    def get_discount(self, product):
        """ значение дисконта на продукт у покупателя """
        return 1

    def discount_pct(self, product):
        return round(100 - 100 * self.get_discount(product))

    def set_budget(self, how_mach_money: float):
        """ изменяет бюджет покупателя"""
        # Сложность 4) b) и пополнять бюджет клиента
        self.budget = round(self.budget + how_mach_money, ndigits=2)


class VipBuyer(Buyer):
    """ Vip покупатель скидка 20% """

    def __init__(self, name: str, budget: float):
        super().__init__(name=name, budget=budget)

    def get_discount(self, product):
        """ значение дисконта на продукт у покупателя """
        return super().get_discount(product) * product.discount


class SuperVipBuyer(VipBuyer):
    """ SuperVip покупатель скидка 36% """

    def __init__(self, name: str, budget: float):
        super().__init__(name=name, budget=budget)

    def get_discount(self, product):
        """ значение дисконта на продукт у покупателя """
        return super().get_discount(product) * product.discount


if __name__ == "__main__":
    # начальные данные ------------------------------------------------------------------
    bread = Product(name='Bread', price=10, in_stock=200)
    wine = Product(name='Wine', price=60, in_stock=200)
    pepper = Product(name='pepper', price=10, in_stock=100)
    grecha = VipProduct(name=' grecha', price=10, in_stock=100)

    usr = Buyer(name="Petro", budget=100)
    vip_usr = VipBuyer(name="Pavlo", budget=100)
    super_vip_user = SuperVipBuyer(name="Stepan", budget=100)
    user_list = [usr, vip_usr, super_vip_user]

    # сколько продуктов одного вида пользователь может купить ------------------------------------------------------

    # print(usr.get_quantity_of_product(product=bread))
    # print(vip_usr.get_quantity_of_product(product=bread))
    # print(super_vip_user.get_quantity_of_product(product=bread))

    # print(usr.get_quantity_of_product(product=grecha))
    # print(vip_usr.get_quantity_of_product(product=grecha))
    # print(super_vip_user.get_quantity_of_product(product=grecha))
    #
    # print(usr.get_quantity_of_product(product=pepper))
    # print(vip_usr.get_quantity_of_product(product=pepper))
    # print(super_vip_user.get_quantity_of_product(product=pepper))

    # покупка продуктов ------------------------------------------------------------------
    what = bread
    how = 11
    for user in user_list:
        print(f"До: у {user.name} {user.budget} денег | на складе {what.in_stock} {what.name}")
        print(f"{user.name} хочет купить {how} {what.name} по цене {what.price} c дисконтом {user.discount_pct(what)}%")
        print(f"результат {user.buy(what, how)}")
        print(f"После: у {user.name} {user.budget} денег | на складе {what.in_stock} {what.name}\n")
