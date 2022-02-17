class Singleton:
    """
    Make a one instance from this class
    if you have been created one object from this class 
    after that if you want to create another one python interpreter
    will be returned the reference of first object did you create
    
    """

    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


s1 = Singleton()
s2 = Singleton()
print(s1 == s2)
