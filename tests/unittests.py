"""
LLM Used: 'ChatGPT 4o mini'
"""
from PlainTools import *

import unittest

class TestPlainTools(unittest.TestCase):

    def test_plist(self):
        # Test with mixed iterable types
        self.assertEqual(plist((1, 2), [3, 4], {5, 6}), [1, 2, 3, 4, 5, 6])
        self.assertEqual(plist({0: 10, 1: 20, 2: 40}), [10, 20, 40])
        self.assertEqual(plist({'A': 10, 'B': 15, 'C': 20, 'D': {"X": 100, "Y": 200, "Z": 300}}),
                         [10, 15, 20, 100, 200, 300])
        # Test with nested structures
        self.assertEqual(plist([1, (2, {3: 4}), [5, {6, 7}]]), [1, 2, 4, 5, 6, 7])
        # Test with empty input
        self.assertEqual(plist(), [])

    def test_punit(self):
        # Test with various iterable inputs
        self.assertEqual(punit([5], [3, 2], [[9]]), (5, [3, 2], 9))
        self.assertEqual(punit([1, 2], 3, (4,)), ([1, 2], 3, 4))
        # Test with no iterable input
        self.assertEqual(punit(), None)
        # Test with single element
        self.assertEqual(punit([1]), 1)
        # Test with multiple single elements
        self.assertEqual(punit(1, 2, 3), (1, 2, 3))

    def test_pnumber(self):
        # Test with numeric values and expressions
        self.assertEqual(pnumber([8.0, '0.1 * 3', '355/113', 'math.e']),
                         [8, 0.3, 3.1415929203539825, 2.718281828459045])
        self.assertEqual(pnumber(1/3, 10/33, 100/333, 1000/3333),
                         [0.3333, 0.3030303, 0.3003003003, 0.3000300030003])
        self.assertEqual(pnumber(0.1 ** 1e-12), 0.9999999999977)
        self.assertEqual(pnumber(0.1 ** 32), 0)
        self.assertEqual(pnumber(0.1 ** 32, tol=32), 1e-32)
        # Test with invalid input
        self.assertEqual(pnumber('invalid'), None)

    def test_pdecimals(self):
        # Test with various numbers
        self.assertEqual(pdecimals(1.23, 4.5678, 3.1, 5.67890), 4)
        self.assertEqual(pdecimals(1/3), 4)
        self.assertEqual(pdecimals(math.pi), 15)
        # Test with a mix of numbers and strings representing numbers
        self.assertEqual(pdecimals('0.123', 1.2, 3.4567), 4)
        # Test with integer inputs
        self.assertEqual(pdecimals(1, 2, 3), 0)
        # Test with empty input
        self.assertEqual(pdecimals(), 0)

    def test_pstring(self):
        # Test with various types of input
        self.assertEqual(pstring({0: 'a', 1: 'b', 2: 'c'}), '0 : a, 1 : b, 2 : c')
        self.assertEqual(pstring([1, 2, 3], (4, 5), {6, 7}), '1, 2, 3, 4, 5, 6, 7')
        self.assertEqual(pstring('Hello', ['world', '!'], sep=' '), 'Hello world !')
        # Test with mixed types and separators
        self.assertEqual(pstring(['Hello', 'world'], 123, sep=' - '), 'Hello - world - 123')
        # Test with empty input
        self.assertEqual(pstring(), '')

    def test_pistype(self):
        # Test with various objects and types
        self.assertEqual(pistype('Hello', str, Iterable, Set), (True, True, False))
        self.assertEqual(pistype([1, 2, 3], List, Tuple, Iterable), (True, False, True))
        self.assertEqual(pistype(42.0, Number, int, float), (True, False, True))
        # Test with multiple types
        self.assertEqual(pistype(42, int, float, str), (True, False, False))
        # Test with objects not matching any type
        self.assertEqual(pistype(42, str, list), (False, False))
        
    def test_prange(self):
        # Test with different combinations of arguments
        self.assertEqual((prange(5)), [0, 1, 2, 3, 4, 5])
        self.assertEqual(prange(5, 2.5, 0.5, 'tuple'), (5, 4.5, 4, 3.5, 3, 2.5))
        self.assertEqual((prange(0, 15, 4, 'dict')), {0: 0, 1: 4, 2: 8, 3: 12})
        self.assertEqual((prange(0, 10, 2)), [0, 2, 4, 6, 8, 10])
        self.assertEqual((prange(10, 0, -2)), [10, 8, 6, 4, 2, 0])
        self.assertEqual((prange(10, 0, -2, 'set')), {0, 2, 4, 6, 8, 10})
        self.assertEqual((prange(10, 0, -2, 'dict')), {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 0})

    def test_pinterval(self):
        # Test with different combinations of arguments
        self.assertEqual((pinterval(5)), [0, 25, 50, 75, 100])
        self.assertEqual((pinterval(3, 5)), [0, 2.5, 5])
        self.assertEqual((pinterval(5, 10, 0, 'dict')), {0: 10, 1: 7.5, 2: 5, 3: 2.5, 4: 0})
        self.assertEqual((pinterval(5, 1, 5)), [1, 2, 3, 4, 5])
        self.assertEqual((pinterval(3, 0, 10)), [0, 5, 10])
        self.assertEqual((pinterval(4, 10, 100, 'tuple')), (10, 40, 70, 100))

    def test_psequence(self):
        # Test with different patterns and limits
        self.assertEqual(list(psequence(1, 2, 3, ..., 10)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(list(psequence(-1, -3, ..., -10)), [-1, -3, -5, -7, -9])
        self.assertEqual(list(psequence(10e-6, abs_lim=50e-6)), [10e-6, 20e-6, 30e-6, 40e-6, 50e-6])

    def test_pindex(self):
        # Test with different iterables
        self.assertEqual(pindex(True, (False, False, True)), 2)
        self.assertEqual(pindex(5, range(10)), 5)
        self.assertEqual(pindex(1, (False, False, True), ['a', 'b', 'c'], range(10)), (2, None, 1))
        self.assertEqual(pindex('d', 'abc', 'def'), (None, 0))
        self.assertEqual(pindex('z', 'abc', 'def'),( None, None))
        self.assertEqual(pindex(2.5, [1.0, 2.5, 3.0]), 1)

    def test_pminmax(self):
        # Test with various values
        self.assertEqual(pminmax([5, 2, -8, '15*2']), {'min': -8, 'max': 30})
        self.assertEqual(pminmax(1, -2, ['1.5 * 2'], math.pi), {'min': -2, 'max': 3.141592653589793})
        self.assertEqual(pminmax(1, 2, 3, 4), {'min': 1, 'max': 4})
        self.assertEqual(pminmax([10, 20, 30]), {'min': 10, 'max': 30})
        self.assertEqual(pminmax(['10', '20', '30']), {'min': 10, 'max': 30})  # Assuming pnumber handles this correctly

    def test_plen(self):
        # Test with different iterables
        self.assertEqual(plen([1, 2, 3], (4, 5), {6}), {'min': 1, 'max': 3})
        self.assertEqual(plen([1, 2, 3, [4, 5], 6], "ABCDEFGHIJ", "XYZ", {}), {'min': 0, 'max': 10})
        self.assertEqual(plen({0: 1, 1: -2, 2: 4, 3: -8, 4: 16, 5: 32}), {'min': 6, 'max': 6})
        self.assertEqual(plen([], [], (1, 2)), {'min': 0, 'max': 2})
        self.assertEqual(plen('short', 'longer', 'longest'), {'min': 5, 'max': 7})

    def test_pabs(self):
        # Test with different sets of numbers and strings
        self.assertEqual(pabs([5, 8, -2, '15*2']),
                         {'min':2, 'max':30, 'ogmin':-2, 'ogmax': 30})
        self.assertEqual(pabs(-1, -2, ['1.5 * 2'], math.pi),
                         {'min': 1, 'max': 3.141592653589793, 'ogmin': -2, 'ogmax': 3.141592653589793})
        self.assertEqual(pabs(prange(-10, 0, 1)),
                         {'min': 0, 'max': 10, 'ogmin': -10, 'ogmax': 0})
        self.assertEqual(pabs([1, 0.5, -2.5]), {'min': 0.5, 'max': 2.5, 'ogmin': -2.5, 'ogmax': 1})

    def test_psum(self):
        # Test with different sets of numbers and strings
        self.assertEqual(psum([5, 2, -8, '15*2']), 29)
        self.assertEqual(psum(prange(-10, 0)), -55)
        self.assertEqual(psum(Container(John=2.55, Maria=3.14, Paul=1.75)), 7.44)
        self.assertEqual(psum([1, 2, 3]), 6)
        self.assertEqual(psum(['1', '2', '3']), 6)  # Assuming pnumber handles this correctly

    def test_pimport(self):
        # Test importing modules and functions
        math_module = pimport('math')
        self.assertEqual(math_module, math)
        pi, log = pimport('math', 'pi, log')
        self.assertEqual(pi, math.pi)
        self.assertEqual(log, math.log)
        # Testing invalid imports
        invalid_import = pimport('non_existent_module')
        self.assertIsNone(invalid_import)

    def test_pframe(self):
        # Test getting frame information
        frame = pframe()
        self.assertEqual(frame.f_lineno, inspect.currentframe().f_lineno)
        self.assertEqual(frame.f_code.co_name, 'test_pframe')

    def test_let(self):
        # Test variable assignments and their values
        result = let(x=5, y=10, z=5 + 10)
        self.assertEqual(result['x'], 5)
        self.assertEqual(result['y'], 10)
        self.assertEqual(result['z'], 15)
        
        # Testing with complex expressions
        import math
        result = let(a=math.pi, b='a', c=2 * 3.5)
        self.assertEqual(result['a'], math.pi)
        self.assertEqual(result['b'], 'a')
        self.assertEqual(result['c'], 7.0)
        
        # Check if variable assignment is handled correctly
        with self.assertRaises(NameError):
            let(x=1, y=x + 1)  # x is not defined within this call

    def test_const(self):
        # Test constant assignments and their values
        result = const(x=2.5, y=3.5)
        self.assertEqual(result['x'], Constant(2.5))
        self.assertEqual(result['y'], Constant(3.5))
        
        # Testing with complex data types
        result = const(z=[0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(result['z'], Constant([0, 1, 1, 2, 3, 5, 8, 13]))
        
        # Check if constant assignment is handled correctly
        with self.assertRaises(NameError):
            const(x=1, y=x + 1)  # x is not defined within this call

if __name__ == "__main__":
    unittest.main()
