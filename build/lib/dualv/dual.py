class Dual:
    
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    @classmethod
    def diff_dual(cls, real):
        return cls(real, 1)

    def __str__(self):
        return f"{self.real} + {self.dual}*eps"

    def __add__(self, second):
        if isinstance(second, (int, float)):
            return Dual(second + self.real, self.dual)
        elif isinstance(second, Dual):
            return Dual(self.real + second.real, self.dual + second.dual)
        return NotImplemented

    def __radd__(self, second):
        return self.__add__(second)

    def __sub__(self, second):
        if isinstance(second, (int, float)):
            return Dual(self.real - second, self.dual)
        elif isinstance(second, Dual):
            return Dual(self.real - second.real, self.dual - second.dual)
        return NotImplemented
   
    def __rsub__(self, second):
        if isinstance(second, (int, float)):
            return Dual(second - self.real, -self.dual)
        elif isinstance(second, diff_dual):
            return Dual(second.real - self.real, second.dual - self.real)
        return NotImplemented

    def __mul__(self, second):
        if isinstance(second, (int, float)):
            return Dual(second*self.real, second*self.dual)
        elif isinstance(second, Dual):
            return Dual(self.real * second.real, self.real * second.dual + self.dual * second.real)
        return NotImplemented

    def __rmul__(self, second):
        return self.__mul__(second)

    def __truediv__(self, second):
        if isinstance(second, (int, float)):
            return Dual(self.real/second, self.dual/second)
        elif isinstance(second, Dual):
            return Dual(self.real / second.real, (self.dual * second.real - self.real * second.dual) / (second.real ** 2))
        return NotImplemented

    def __rtruediv__(self, second):
        if isinstance(second, (int, float)):
            return Dual(second / self.real, -second * self.dual / (self.real ** 2))
        elif isinstance(second, Dual):
            return Dual(second.real / self.real, (second.dual * self.real - second.real * self.dual) / (self.real ** 2))
    
    def __eq__(self, second):
        return (self.real == second.real) and (self.dual == second.dual)

    def __ne__(self, second):
        return (self.real != second.real) or (self.dual != second.dual)

    def __neg__(self):
        return Dual(-self.real, -self.dual)
