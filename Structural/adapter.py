from Creational.AbstractFactory import Rugs


class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        """
        We Have alot of Rugs products and their price tagged by
        USD, and We decide to change it to USD, Have been entered the
        data daily in RIAL (Imaging without vacillation).? NOP !
        we should make an adapter like Cable Adapting to compatible to objects
        or Classes
        :param product:
        :return in daily rate from USD base:
        """
        return self.rate * product._price


if __name__ == "__main__":
    r1 = Rugs('Persian rugs', 20, 'Car')
    r2 = Rugs('Nain rugs', 23, 'Motor')
    r3 = Rugs('Morrocco rugs', 19, 'In door')

    adapter = PriceAdapter(rate=28000)

    rugs = [r1, r2, r3]

    for rug in rugs:
        print(f"{rug._name}: {adapter.exchange(rug)} IRR ")
