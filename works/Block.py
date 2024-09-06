import PlainToolsB as pt

# Test cases for detect_repeating_decimal
test_cases = [
    (0.1666666666666667, '6'),     # Simple repeating single digit
    (0.5858585858585858, '58'),    # Simple repeating two digits
    (0.14285714285714285, '142857'),# Long repeating sequence
    (0.123123123123123, '123'),    # Repeating three digits
    (0.0909090909090909, '09'),    # Repeating two digits
    (0.0101010101010101, '01'),    # Repeating two digits
    (0.2727272727272727, '27'),    # Simple repeating two digits
    (0.999999999999999, '9'),      # Simple repeating single digit
    (1.4142135623730951, pt.Null),    # Non-repeating irrational number (square root of 2)
    (0.5555555555555556, '5'),     # Repeating single digit
    (1.3333333333333333, '3'),     # Repeating single digit after integer
    (0.4444444444444444, '4'),     # Repeating single digit
    (2.777777777777778, '7'),      # Repeating single digit after integer part
    (0.123456789123456, pt.Null),     # No repeating pattern, unique sequence
    (0.999950000499995, pt.Null),     # No repeating pattern, almost 1 but with precision issues
    (0.6767676767676768, '67'),    # Repeating two digits
    (0.00101010101010101, '01'),   # Repeating two digits, after leading zeroes
    (5.666666666666667, '6'),      # Repeating single digit after integer part
    (3.125125125125125, '125'),    # Repeating three digits after integer part
    (0.8888888888888888, '8'),      # Repeating single digit
    (1/3, '3'),
    (10/33, '30'),
    (100/333, '300'),
    (1000/3333, '3000'),
    (10000/33333, '30000'),
    (100000/333333, '300000'),
    (22/7, '142857'),
    (1/9, '1'),
    (7/12, '3'),
]

for num, expected in test_cases:
    print(f"Number: {pt.Number(num)}\nPeriod: {(expected*3)+'...'}\nGot: {((pt.Number(num).period)*3)+'...'}\n")
