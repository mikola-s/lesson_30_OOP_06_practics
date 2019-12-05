from math import trunc


class WhereIsMoney(Exception):
    pass


class WhatProduct(Exception):
    pass


class Product:
    def __init__(self, name: str, price: float, count: int = 10, discount: float = 1):
        self.name = name
        self.price = price
        self.discount = discount
        self.count = count


class VipProduct(Product):
    def __init__(self, name: str, price: float, count: int = 10, discount: float = 1):
        super().__init__(name, price, count, discount)


class Buyer:
    def __init__(self, budget: float):
        self.budget = self.check_budget(budget)

    def get_product_count(self, product: Product):
        if isinstance(product, Product):
            offset = product.count - trunc(self.budget / product.price)
            if offset >= 0:
                product.count = offset
                return trunc(self.budget / product.price)
            else:
                temp = product.count
                product.count = 0
                return temp
        else:
            raise WhatProduct('что покупаешь?')

    @staticmethod
    def check_budget(budget):
        if isinstance(budget, str):
            if budget.isdigit():
                budget = float(budget)
            else:
                budget = 0
        if (isinstance(budget, float) or isinstance(budget, int)) and budget < 0:
            budget = 0
        return budget


class VipBuyer(Buyer):
    def __init__(self, budget: float):
        super().__init__(budget)

    def get_product_count(self, product: Product):
        return trunc(super().get_product_count(product) / product.discount)


class SuperVipBuyer(VipBuyer):
    def __init__(self, budget: float):
        super().__init__(budget)

    def get_product_count(self, product: Product):
        return trunc(super().get_product_count(product) / product.discount)


bread = Product('Bread', 20, count=200, discount=0.8)
wine = Product('Wine', 60, count=200, discount=0.8)

grecha = VipProduct(name='Grecha', price=10, count=100)

usr = Buyer(budget=200)
vip_usr = VipBuyer(budget=200)
super_vip_user = SuperVipBuyer(budget=200)

print(usr.get_product_count(product=bread))
print(vip_usr.get_product_count(product=bread))
print(super_vip_user.get_product_count(product=bread))

print(usr.get_product_count(product=grecha))
print(vip_usr.get_product_count(product=grecha))
print(super_vip_user.get_product_count(product=grecha))

peper = Product('pepper', 10, count=100)

print(usr.get_product_count(product=peper))
print(vip_usr.get_product_count(product=peper))
print(super_vip_user.get_product_count(product=peper))
