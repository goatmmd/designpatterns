from abc import ABC, abstractmethod

COUNTRIES = ['Iran', 'UAE']
VAT = {
    "Iran": 9,
    "UAE": 15
}


class UserBase(ABC):
    _id = 0

    def __init__(self):
        self.id = self.generate_id()

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id


class User(UserBase):
    def __init__(self, name, address):
        self.address = address
        self.name = name
        super().__init__()


class Address:
    def __init__(self, name):
        self.name = name


class ProductsBase(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def show_detail(self):
        pass


class Products(ProductsBase):
    def __init__(self, name, price):
        super().__init__(name, price)

    @property
    def show_detail(self):
        return f"{self.name}: {self.price}$"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.product_list = list()

    def add_product(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]
        self.product_list.extend(product_list)

    @property
    def total_price(self):
        """
        Decorator pattern will be adding an advantage to object(like this "look at code")
        without change the structural of our obj or method, usually we apply this pattern
        in python with Decorator adjective , ATTENTION: Decorator pattern isn't Decorator adjective in python
        these are not same....!
        :return:
        """
        s = 0
        for product in self.product_list:
            s += product.price
        return s


def calculate_vat(fun):
    def wrapped_func(pur):
        vat = VAT[pur.user.address.name]
        total_price = fun(pur)
        return f"User {pur.user.id} buy from {pur.user.address.name} total price: {total_price + total_price * vat // 100}"

    return wrapped_func


@calculate_vat
def show_total_price(obj):

    return obj.total_price


if __name__ == "__main__":
    add_iran = Address(COUNTRIES[0])
    user1 = User('user', add_iran)
    p1 = Products("P1", 120)
    p2 = Products("P2", 130)
    p3 = Products("P3", 200)
    products = [p1, p2]

    purchase = Purchase(user1)

    purchase.add_product(p1)
    # print(purchase.total_price())
    purchase.add_product(products)

    print(show_total_price(purchase))
