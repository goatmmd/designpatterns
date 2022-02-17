"""
    The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms,
    encapsulates each one and putting each of them into separate classes and also allows to interchange there objects.
    It is implemented in Python by dynamically replacing the content of a method defined inside
    a class with the contents of functions defined outside of the class.
    It enables selecting the algorithm at run-time. This method is also called as Policy Method.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"


class Gateway:
    def __init__(self, name):
        self.name = name


class Payment:
    gateway = [Gateway("PasarGard"), Gateway("Saman")]

    def __init__(self, purchase):
        self.purchase = purchase

    def check_gateway(self):
        return self.gateway[0] if self.purchase.total_price > 100 else self.gateway[1]

    def pay(self):
        gateway = self.check_gateway()
        print(f"{gateway.name} for {self.purchase.products}")


class Purchase:
    def __init__(self):
        self.products = list()
        self.payment = Payment(self)

    def add(self, product):
        if isinstance(product, list):
            self.products.extend(product)
        else:
            self.products.append(product)

    def total_price(self):
        total = list()
        for product in self.products:
            total.append(product.price)
        return sum(total)

    def check_out(self):
        self.payment.pay()


if __name__ == "__main__":
    p1 = Product('p1', 100)
    p2 = Product('p2', 120)
    p3 = Product('p3', 140)

    purchase = Purchase()
    purchase.add([p2, p1])
    print(purchase.total_price())
    purchase.check_out()
