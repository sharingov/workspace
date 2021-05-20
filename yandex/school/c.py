class PearsBasket:

    def __init__(self, pears):
        self.pears = pears

    def __floordiv__(self, n):
        basket = [PearsBasket(self.pears // n)] * n
        if self.pears % n != 0:
            basket.append(PearsBasket(self.pears % n))
        return basket

    def __mod__(self, n):
        return self.pears % n

    def __add__(self, pb):
        return PearsBasket(self.pears + pb.pears)

    def __sub__(self, n):
        self.pears = max(0, self.pears - n)

    def __str__(self):
        return(str(self.pears))

    def __repr__(self):
        return("{name}({pears})".format(name=type(self).__name__, pears=self.pears))
