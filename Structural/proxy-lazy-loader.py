class LazyLoader:
    """
    That is Lazy Loader,  it will load your object lazy !!!!
    it will load your object when you actually need to them (when you called the method of those object)
    Now will be loaded ...
    This is kind of Proxy pattern in Lazy Loader purport
    """

    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySQLHandler:
    def __init__(self):
        print('HERE')

    def get(self):
        return "Hello From MySql"


if __name__ == "__main__":
    mq = LazyLoader(MySQLHandler)

    print(mq.get())
