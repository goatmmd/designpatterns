from observer.observers import EmailNotification, SMSNotification
from observer.decorator import send_notification


class Product:
    pass


class Purchase:
    observers = [EmailNotification, SMSNotification]

    def __init__(self, product):
        self.products = product
        self.is_paid = False

    @send_notification('Purchase Paid')
    def check_out(self):
        self.is_paid = True

    @send_notification('Purchase Cancel')
    def cancel(self):
        pass
