import PlainToolsB as pt
import re

if True:
    def REP(num):
        """
        Detect repeating decimal patterns in a given number.

        :param num: The number to detect repeating decimals in.
        :return: The repeating decimal pattern, or None if no valid pattern is found.
        """
        if float(num).is_integer():
            return None
        
        num_str = repr(num)
        if 'e' in num_str:
            num_str = format(float(
                num_str), f".{abs(int(num_str.split('e')[1])) + 15}f")

        # Extract decimal part
        decimal_part = num_str.split('.')[1].rstrip('0')[:15]
        
        # Check for repeating patterns starting from any position in the decimal part
        for start_idx in range(len(decimal_part)):
            sub_decimal_part = decimal_part[start_idx:]
            for pattern_length in range(1, 7):  # Extend pattern length for longer sequences
                regex = re.compile(rf"(\d{{{pattern_length}}})\1+")
                match = regex.search(sub_decimal_part)
                if match:
                    repeat_str = match.group(1)
                    repeat_count = len(match.group(0)) // len(repeat_str)
                    remaining_digits = sub_decimal_part[match.end():]

                    # Allow one insignificant digit at the end
                    if len(remaining_digits) <= 1:
                        if (pattern_length == 1 and repeat_count >= 6) or \
                        (pattern_length == 2 and repeat_count >= 5) or \
                        (pattern_length == 3 and repeat_count >= 4) or \
                        (pattern_length == 4 and repeat_count >= 3) or \
                        (pattern_length == 5 and repeat_count >= 2) or \
                        (pattern_length == 6 and repeat_count >= 1):  # For longer patterns
                            # Exclude '0' and '9' as repeating periods
                                return repeat_str if all(
                                    rp!=0 or rp!=9 for rp in repeat_str) and (
                                repeat_str!='0' and repeat_str!='9') else None

        return None

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
    (1.4142135623730951, None),    # Non-repeating irrational number (square root of 2)
    (0.5555555555555556, '5'),     # Repeating single digit
    (1.3333333333333333, '3'),     # Repeating single digit after integer
    (0.4444444444444444, '4'),     # Repeating single digit
    (2.777777777777778, '7'),      # Repeating single digit after integer part
    (0.123456789123456, None),     # No repeating pattern, unique sequence
    (0.999950000499995, None),     # No repeating pattern, almost 1 but with precision issues
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
    (1000000/3333333, '3000000'),
    (22/7, '142857'),
    (1/9, '1'),
    (7/12, '3'),
    (1/14, '?'),
]

for num, expected in test_cases:
    print(f"Number: {pt.Number(num)}\nPeriod: {expected}\nGot: {pt.Number(num).period}\n")
