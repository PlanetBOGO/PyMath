import math
def root(num, root):
    return(num**(1/root))
class Radical(object):
    """Radical
    Vars:
        num
        root
    """
    #Do not develop
    def __init__(self, num, root, coef = 1):
        self.num = num
        self.root = root
        self.coef = coef
        self.reduce()
        print("New Radical %s" % self);
        return
    def __del__ (self, *args, **kwargs):
        print("Deleted Radical %s" % self)
        return
    def __str__(self):
        return "root %s of %s" % (self.root, self.num)
    # remake __CMP__
    def __cmp__(self, other):
        return (root(self.num, self.root), root(other.num, other.root))
    def val (self):
        return root(self.num, self.root)
    def __abs__(self):
        return Radical(abs(self.num), self.root)
    def __add__(self, other):
        if isinstance(other, Radical):
            toAdd = other.reduce()
            if toAdd.num == self.num and toAdd.root == self.root:
                return Radical(self.num, self.root, self.coef+toAdd.coef)
            return [self, toAdd]
        return [self, other]
    def __sub__ (self, other):
        if isinstance(other, Radical):
            toSub = other.reduce()
            if toSub.num == self.num and toSub.root == self.root:
                return Radical(self.num, self.root, self.coef-toSub.coef)
            return [self, toSub]
        return [self, -other]
    def __mul__ (self, other):
        if isinstance(other, Radical):
            if other.root == self.root:
                return Radical(self.num*other.num, self.root, self.coef*other.coef)
            else:
                return [self, other]
        return Radical(self.num, self.root, self.coef*other)
    def __truediv__ (self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num*other.denom, self.denom*other.num)
        return self.__truediv__(Fraction(other, 1))
    def recip (self):
        return Fraction(self.denom, self.num)
    def __pow__ (self, other):
        return Fraction(self.num**other, self.denom**other)
    def __rpow__(self, other):
        return other**self.val()
    def __float__ (self):
        return self.val
    def __nonzero__(self):
        if self.num != 0 : return True
        return False
    def reduce(self):
        raise Exception
    def __radd__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num*other.denom + self.denom*other.num, self.denom * other.denom )
        return self.__radd__(Fraction(other, 1))
    def __rsub__ (self, other):
        if isinstance(other, Fraction):
            return Fraction(self.denom*other.num - self.num*other.denom , self.denom*other.denom)
        return self.__rsub__(Fraction(other, 1))
    def __rmul__ (self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom*other.denom)
        return self.__rmul__(Fraction(other, 1))
    def __rtruediv__ (self, other):
        if isinstance(other, Fraction):
            return Fraction(self.denom*other.num, self.num*other.denom)
        return self.__rtruediv__(Fraction(other, 1))
    def __pos__(self):
        return +self.num
    def __neg__(self):
        return -self.num
    def __bool__(self):
        if self.num!=0: return True
        return False
