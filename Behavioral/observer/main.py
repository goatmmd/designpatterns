from observer.shop import Purchase, Product

if __name__ == "__main__":
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()

    pur = Purchase([p1, p2, p3, p4])
    pur.cancel()
    pur.check_out()
