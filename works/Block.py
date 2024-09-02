from PlainToolsB import *

class OldFloat(float): pass

class NewFloat(float):
    def inverse(self):
        return OldFloat(-self)

@arithmetic(repr="{value}")
class RealNumber:
    value = lambda n: pnumber(n)
    
x = RealNumber(4.2)

print(x)
print(type(x))
print(type(x.is_integer()))

y = RealNumber('foofoo')

print(y)