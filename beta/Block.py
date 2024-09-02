from PlainToolsB import *

class OldFloat(float): pass

class NewFloat(float):
    def inverse(self):
        return OldFloat(-self)

@arithmetic(repr="{value}", strict=True)
class RealNumber:
    value: Real = lambda n: pnumber(n)
    
x = RealNumber(4.2)

print(x)
print(type(x))
print(type(x.is_integer()))

y = RealNumber('foofoo')

print(y)