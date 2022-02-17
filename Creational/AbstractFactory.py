from abc import ABC, abstractmethod


class ProductBase(ABC):
    """
    AbstractFactor : That means you should create an interface
    for your script to develop easy in future Now you can look at the code
    actually AF that allows you to produce the families of related objects without specifying their concrete classes.
    Using the abstract factory method, we have the easiest ways to produce a similar type of many objects.

    """

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def shipping(self):
        pass


class Rugs(ProductBase):
    def __init__(self, name, price, shipping):
        self._name = name
        self._price = price
        self._shipping = shipping

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)

    @property
    def shipping(self):
        return RugsDetail(self)


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


class RugsDetail(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"Rugs Name : {self.rugs._name} {self.rugs._shipping}"


class RugsPrice(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"Rugs price : {self.rugs._price}"


if __name__ == "__main__":
    r1 = Rugs('persian rugs', 130, 'Car')
    r2 = Rugs('Morrow rugs', 120, 'Car')

    products = [r1, r2]

    for product in products:
        print(product.price.show())
        print(product.detail.show())
