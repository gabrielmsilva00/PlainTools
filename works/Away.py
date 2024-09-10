
import PlainToolsB as pt

def float_imprecision_test(fn, test=('',)):
    
    for test in tests:
        try:
            print(f'{fn.__name__}({test}) == {fn(test)}')
        except BaseException as e:
            print(f'{fn.__name__}({test}) == {e}')
            print('ERROR')
        finally:
            print(f'eval({test}) == {pt.Seval(test)}')
            print()

tests = (
    "0.1 * 3",  # Classic example
    "0.1 * 7",
    "5/3",
    "0.1 + 0.2",  # Another classic example
    "0.3 - 0.1",
    "1.2 - 1.0",
    "0.1 + 0.1 + 0.1 - 0.3",
    "1e-8 + 1 - 1",  # Small number addition
    "1e100 + 1 - 1e100",  # Large number addition
    "0.1234567890123456 + 1e-16",  # Precision loss
    "1 / 3 * 3",
    "0.1 ** 3",  # Powers
    "355 / 113",  # Approximation of pi
    "2 ** 53 + 1 - 2 ** 53",  # Beyond integer precision
    "0.1 * 10 ** 16 - 10 ** 15",
    "0.3333333333333333 * 3",
    "1e-16 * 1e16 - 1",
    "1e16 + 1 - 1e16",
    "0.1 * 0.1",
    "0.000000000000001 + 1 - 1",
    "9999999999999999 + 0.00000000000001 - 9999999999999999",
    "0.2 * 0.2",
    "0.5 - 0.4 - 0.1",
    "1e-323 + 1e-323",  # Near smallest representable double
    "1.7976931348623157e+308 + 1 - 1.7976931348623157e+308",  # Near largest representable double
    "1 / 10 + 1 / 100 + 1 / 1000",
    "0.1 + 0.01 + 0.001 + 0.0001 + 0.00001",
    "math.sin(math.pi/2)",  # Trigonometric functions (assuming math.sin and math.pi are imported)
    "math.log(math.exp(1))",  # Logarithmic and exponential functions (assuming math.log and math.exp are imported)
    "math.sqrt(2) ** 2 - 2",  # Square root (assuming math.sqrt is imported)
)

float_imprecision_test(pt.number, tests)