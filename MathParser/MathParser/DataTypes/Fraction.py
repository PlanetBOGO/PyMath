class Fraction(object):
    """Fraction"""

    #Methods
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        print("New Fraction %s" % self)
        return
    def __del__(self):
        print("Deleted Fraction %s" % self)
        return
    def __str__(self):
        return "%s/%s" % (self.num, self.denom)
    def __cmp__(self, other):
        return (cmp(self.num / self.denom, other.num / other.denom))
    def val(self):
        if  type(self.num) is int or type(self.num) is float:
            numval = self.num
        if type(self.denom) is int or type(self.denom) is float:
            denomval = self.denom
        else:
            numval = self.num.val()
            denomval = self.denom.val()
        return numval / denomval
    def asPercent(self):
        return self.num / self.denom * 100
    def __abs__(self):
        return Fraction(abs(self.num), abs(self.denom))
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)
        return self.__add__(Fraction(other, 1))
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom - self.denom * other.num, self.denom * other.denom)
        return self.__sub__(Fraction(other, 1))
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom * other.denom)
        return self.__mul__(Fraction(other, 1))
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom, self.denom * other.num)
        return self.__truediv__(Fraction(other, 1))
    def recip(self):
        return Fraction(self.denom, self.num)
    def __pow__(self, other):
        return Fraction(self.num ** other, self.denom ** other)
    def __rpow__(self, other):
        return other ** self.val()
    def __float__(self):
        return self.val
    def __nonzero__(self):
        if self.num != 0 : return True
        return False
    def reduce(self):
        raise Exception
    def __radd__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)
        return self.__radd__(Fraction(other, 1))
    def __rsub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.denom * other.num - self.num * other.denom , self.denom * other.denom)
        return self.__rsub__(Fraction(other, 1))
    def __rmul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom * other.denom)
        return self.__rmul__(Fraction(other, 1))
    def __rtruediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.denom * other.num, self.num * other.denom)
        return self.__rtruediv__(Fraction(other, 1))
    def __pos__(self):
        return Fraction(+self.num, self.denom)
    def __neg__(self):
        return Fraction(-self.num, self.denom)
    def __bool__(self):
        if self.num != 0: return True
        return False
