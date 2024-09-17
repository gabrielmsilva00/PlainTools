import PlainTools as pt
import PlainToolsB as ptb

# Test cases for detect_repeating_decimal
test_literals = [
    ('0.1666666666666667', '6'),     # Simple repeating single digit
    ('0.5858585858585858', '58'),    # Simple repeating two digits
    ('0.14285714285714285', '142857'),# Long repeating sequence
    ('0.123123123123123', '123'),    # Repeating three digits
    ('0.0909090909090909', '09'),    # Repeating two digits
    ('0.0101010101010101', '01'),    # Repeating two digits
    ('0.2727272727272727', '27'),    # Simple repeating two digits
    ('0.5555555555555556', '5'),     # Repeating single digit
    ('1.3333333333333333', '3'),     # Repeating single digit after integer
    ('0.4444444444444444', '4'),     # Repeating single digit
    ('2.777777777777778', '7'),      # Repeating single digit after integer part
    ('0.6767676767676768', '67'),    # Repeating two digits
    ('0.00101010101010101', '01'),   # Repeating two digits, after leading zeroes
    ('5.666666666666667', '6'),      # Repeating single digit after integer part
    ('3.125125125125125', '125'),    # Repeating three digits after integer part
    ('0.8888888888888888', '8'),      # Repeating single digit
    ('0.123456789123456', pt.Null),     # No repeating pattern, unique sequence
    ('0.999950000499995', pt.Null),     # No repeating pattern, almost 1 but with precision issues
    ('0.9999999999999988', pt.Null),      # Simple repeating single digit, no repeating at end.
    ('1.4142135623730951', pt.Null),    # Non-repeating irrational number (square root of 2)
    ("math.pi", pt.Null), # Math literal, no repeating part.
    ("math.e", pt.Null), # Math literal, no repeating part.
]

test_operations = [
    ('1/3', '3'),
    ('10/33', '30'),
    ('100/333', '300'),
    ('1000/3333', '3000'),
    ('10000/33333', '30000'),
    ('100000/333333', '300000'),
    ('1000000/3333333', '3000000'),
    ('1/7', '142857'),
    ('22/7', '142857'),
    ('1/9', '1'),
    ('1/11', '09'),
    ('1/13', '076923'),
    ('2/3', '6'),
    ('1/21', '047619'),
    ('1/27', '037'),
    ('1/33', '03'),
    ('1/37', '027'),
    ('1/41', '02439'),
    ('1/73', '01369863'),
    ('1/91', '010989'),
    ('1/101', '0099'),
    ('2/7', '285714'),
    ('3/11', '27'),
    ('4/13', '307692'),
    ('3/37', '081'),
    ('7/73', '09589041'),
    ('7/12', '3'),
    ('5/3', '6'),
    ('5.0 + 5.123', pt.Null),
    ("math.pi/3", pt.Null),
]

for num, expected in test_literals + test_operations:
    n = ptb.number(num)
    print(
        f"String Evaluated:\t{repr(num)}\n",
        f"Object Instance:\t{n.object}\n",
        f"Number Instance:\t{n}\n",
        f"Expected Period:\t{(expected)+'...'}\n",
        f"Detected Period:\t{((n.period))+'...'}\n",
        sep='',
        )


# for x in pt.psequence(0.1, 0.2, ..., 2):
#     print(x)

# import decimal
# import fractions

# x = pt.number("decimal.Decimal(0.1)")

# pt.printnl(x,
#            x + 5,
#            x.object,
#            x.period,
#            x.fraction,
#            x.id,
#            x.__class__.__name__,
#            pt.pistype(x,
#                     int,
#                     float,
#                     complex,
#                     pt.Decimal,
#                     pt.Real,
#                     pt.Number,
#                     ),
#            )


# x = pt.number(5)
# y = pt.number(5.123)
# z = pt.number(0.1 * 3)
# w = pt.number(complex(0.5, 3))

# print(x)
# print(y)
# print(z)
# print(w)

# print(type(x), isinstance(x, int), isinstance(x, pt.Number))
# print(type(y), isinstance(y, float))
# print(type(x).__name__)
# print(type(x).__class__)

# # print(pt.psequence(0.1))
# # def number(obj):
# #     class IsValue(type):
# #         def __new__(mcls, classname, bases, classdict):
# #             wrapped_classname = '_%s_%s' % ('Numeric', type(obj).__name__)
# #             return type.__new__(mcls, wrapped_classname, (
# #                 type(obj),)+bases, classdict)

# #     class Numeric(metaclass=IsValue):
# #         def __init__(self, val):
# #             self.value = val
    
# #     return Numeric(obj)

# # x = number(5)
# # print(x) # 5
# # print(x.value)
# # print(isinstance(x, int))  # True
# # print(isinstance(x, float))  # False

# # x = number(5.123)
# # print(x) # 5.123
# # print(isinstance(x, int))  # False
# # print(isinstance(x, float))  # True