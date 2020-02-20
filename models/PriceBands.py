from z3 import *


class PriceBands:
    last_price = Int('last_price')
    percentage = Real('percentage')
    last_approved = Bool('last_approved')

    def input(self, price):
        if abs(price - self.last_price) < self.last_price * self.percentage:
            self.last_price = price
            self.last_approved = True
        else:
            self.last_approved = False

    def __init__(self):
        self.last_price = 10
        self.last_approved = False
        self.percentage = 1

    def hyperstate(self):
        return ("1" if self.last_approved else "0") + "_" + str(self.last_price)

    def possible(self):
        return 0 <= self.last_price <= 10 and 0.0 <= self.percentage <= 100.0

    def input_info(self):
        return {
            'price': list(range(1, 100))
        }
