##!python -m autopep8 -i -a -a -a
"""[||-Plain-Tools-||]
ΛΛΛ Gabriel Maia @gabrielmsilva00 - UERJ - Electric Engineering Undergraduate.
=== Utilities, Constructors, Formatters, Debuggers.
‼‼‼ Tooling:
==> AutoPEP8: Code formatting by Python's extension autopep8 -i -a*3.
==> Sphinx: Code has modular, Sphinx-ready (.rst) documentation and typing.

○○○ References and auxiliary material:
••• AutoPEP8, code formatting;
∙∙∙ pypi.org/project/autopep8/
••• Sphinx, documentation;
∙∙∙ sphinx-doc.org
••• StackOverflow, definitions;
∙∙∙ stackoverflow.com
••• W3Schools, theories, fundamentals, methods;
∙∙∙ w3schools.com/python/
••• OpenAI ChatGPT, definitions and debugging;
∙∙∙ chat.openai.com
••• Claude AI, additional debugging;
∙∙∙ claude.ai
••• Codeium AI, autocompletion and code refactoring|cleaning;
∙∙∙ codeium.ai
••• SingleFile extension, HTML factoring;
∙∙∙ chromewebstore.google.com/detail/mpiodijhokgodhhofbcjdecpffjipkle
••• JetBrains Mono, font;
∙∙∙ github.com/JetBrains/JetBrainsMono
"""
# ---------------------------------------------------------------------------<
__version__ = "1.2.241004.0"
__author__ = "gabrielmsilva00"
__url__ = "https://gabrielmsilva00.github.io/PlainTools/"
__repo__ = "https://github.com/gabrielmsilva00/PlainTools.git"


# IMPORTS ==> from <package> import <obj>
import __main__
import os
import sys
import platform
import shutil
import glob
import inspect
import traceback
import collections
import typing
import types
import decimal
import fractions
import numbers
import warnings
import importlib
import re
import ast
import operator
import datetime
import time
import math
import itertools
import functools
import multiprocessing
import copy


# TYPES ==> Special aliases to denote typing annotations; Redundant cases.
Type = type
String = str
Bytes = bytes
Integer = int
Float = float
Complex = complex
Decimal = decimal.Decimal
Fraction = fractions.Fraction
Real = numbers.Real | decimal.Decimal
Number = numbers.Number
Bool = bool

Tuple = tuple
NamedTuple = type(collections.namedtuple)
List = typing.List
Set = collections.abc.Set
Dict = dict
Container = type
Constant = type
Chain = itertools.chain

Iterable = collections.abc.Iterable
Callable = collections.abc.Callable
Module = types.ModuleType
Lambda = types.LambdaType
Function = types.FunctionType
Builtin = types.BuiltinFunctionType
Method = types.MethodType
Decorator = types.MethodWrapperType
Generator = types.GeneratorType
Traceback = types.TracebackType
Frame = types.FrameType
Queue = multiprocessing.Queue
Err = Exception

Any = typing.Any
Object = object
Type = type
Self = typing.Self
Class = type
Args = type
Kwargs = type


# LOGIC ==> Logic gate operators:
Not = lambda *args: tuple(not bool(arg) for arg in args)
Buf = lambda *args: tuple(bool(arg) for arg in args)
And = lambda *args: all(bool(arg) for arg in args)
Nand = lambda *args: not all(bool(arg) for arg in args)
Or = lambda *args: any(bool(arg) for arg in args)
Nor = lambda *args: not any(bool(arg) for arg in args)
Xor = lambda *args: sum(bool(arg) for arg in args) % 2 == 1
Xnor = lambda *args: sum(bool(arg) for arg in args) % 2 == 0


# PLAIN NUMBER ==> Numeric constructor:
def pnumber(*objs: Any | Iterable[Any],
            ) -> Number | List[Number]:
    """
    Plain Numeric Constructor.

    For each input, this function constructs a generic `Numeric` class
    instance which dynamically inherits the input's parent class.
    This means that all numeric types such as 'int', 'float', 'complex',
    'Decimal' and 'Fraction' given to this function will generate a subclass
    instance with inheritance from the object's own numeric class.

    Failure to convert the object to a numeric type (contained into the
    `numbers.Number` definition) will result in an instance of
    `float('nan')` class being returned.

    :Examples:
        Considering `x = pt.pnumber(1/3)`;

        print(x)
            - `0.333...`
            - The `pt.pnumber()` constructor detects repeating decimals.

        x.value
            - `0.3333333333333333`
            - This is used for proper arithmetic operations.

        x.period
            - `3`
            - This is the detected repeating decimal.

        x.fraction
            - `(1, 3)`
            - The fraction part can be used for reconstruction of the object.

        x.type
            - `<class 'float'>`
            - The `x` object dynamically inherited from the `float` class.

        x.id
            - `2667619486224` :grey:`# This is an example`
            - The direct assigned `id()` of the object `float(1/3)`.

    :Args:
        obj: Any | Iterable[Any]
            - Object(s) to `pt.SEVAL(obj)` into a numeric type.
            - Failure to convert to a numeric type will return `float('nan')`.

    :Returns:
        R: Number | List[Number]
            - Numeric-type instance(s) (of `isinstance(obj, numbers.Number)`).
            - The class created dynamically inherits from the `obj` own class.

    :Notes:
        - It is computationally expensive; Not ideal for long sequences.
        - Due to the above, you may want to use 'pt.pround()' instead.

    """
    R: List[Number] = []

    def numeric(obj: Any) -> Number:
        try:
            idobj = id(obj)
            obj = Seval(obj)
            if isinstance(obj, Fraction):
                obj = float(obj)
            if not isinstance(obj, Number):
                obj = float('nan')
        except BaseException:
            obj = float('nan')

        class TypeChecker(type):
            def __new__(mcls, classname, bases, classdict):
                iname = '%s_%s_ID%s' % (
                    classname, type(obj).__name__, id(obj))
                try:
                    R = type.__new__(mcls, iname, (
                        type(obj),) + bases, classdict)
                except TypeError as e:
                    R = type.__new__(mcls, classname, bases, classdict)
                finally:
                    return R

        @arithmetic
        class Numeric(metaclass=TypeChecker):
            def __init__(cls,
                         val: Real | String,
                         ):
                cls.object = obj
                cls.value = cls.number(val)
                cls.period = cls.periodic(cls.value)
                cls.irrational = bool(cls.period)
                cls.type = type(obj)
                cls.string = repr(cls)
                cls.id = id(obj)
                
                try:
                    cls.enot = int(repr(cls).split('e')[1])
                except (IndexError, ValueError):
                    cls.enot = False

                if cls.enot < 0:
                    expo = int(cls.string.split('e-')[-1])
                    expo += len(cls.string.split('.')[-1].split('e')[0])
                    cls.full = f"{cls:.{expo}f}"

                elif cls.enot > 0:
                    intg, inte = repr(cls.value).split('e+')
                    inte = int(inte)
                    while '.' in intg:
                        inta, intb = intg.split('.')
                        inta += intb[0]
                        intb = intb[1:]
                        if intb:
                            intg = inta + '.' + intb
                        else:
                            intg = inta + intb
                        inte -= 1
                        if inte <= 0:
                            break
                    cls.full = str(intg + ('0' * inte))
                    cls.value = Seval(cls.full)

                else:
                    cls.full = repr(cls)

                try:
                    cls.fraction = Fraction(cls.value).limit_denominator(
                        math.ceil(cls.value) * 10e3).as_integer_ratio()
                except Exception:
                    cls.fraction = (float('nan'), float('nan'))

            def __str__(cls):
                if cls.period:
                    strint = repr(cls.value).split('.')[0] + '.'
                    strval = repr(cls.value).split('.')[-1]
                    pstart = strval.find(cls.period)
                    if pstart == -1:
                        return strint + strval + f"{cls.period * 2}..."
                    return strint + strval[
                        :pstart + len(cls.period)] + f"{cls.period * 2}..."
                if And(cls.type == Integer, len(repr(cls.value)) > 15):
                    R, S = str("%.12e" % pround(cls.value, tol=cls.enot)
                               ).split('e')
                    return (R.rstrip('0') + 'e' + S)
                return str(cls.value)

            def __repr__(cls):
                return repr(cls.value)

            def number(cls,
                       num: Real | String,
                       ) -> Real:
                R: Real = float('nan')
                J: Complex = None
                S: Integer = 1

                with Try:
                    # try:
                    R = Seval(num)
                    if isinstance(R, Complex):
                        R, J = R.real, R.imag
                        S += 1

                    elif isinstance(R, Bool):
                        return bool(R)

                    elif And(isinstance(R, (int, float)), float(R).is_integer()):
                        if 'e+' in repr(float(R)):
                            intg, inte = repr(float(R)).split('e+')
                            inte = int(inte)
                            intg = repr(pround(intg, tol=inte))
                            while '.' in intg:
                                inta, intb = intg.split('.')
                                inta += intb[0]
                                intb = intb[1:]
                                if intb:
                                    intg = inta + '.' + intb
                                else:
                                    intg = inta + intb
                                inte -= 1
                                if inte <= 0:
                                    return int(intg)
                            R = int(intg * (10 ** inte))
                        return int(R)

                    elif isinstance(R, (Decimal, Fraction)):
                        R = float(R)

                    while True:
                        SR = repr(R)
                        E = 0

                        if 'e' in SR:
                            SR, E = SR.split('e')[0], int(SR.split('e')[-1])

                        R = pround(float(SR), dcm=16, tol=max(E, 16))

                        if isinstance(R, int):
                            break

                        DP = SR.split('.')[-1][::-1]

                        if len(DP) >= 14:
                            M9 = re.match(r'9+|[0-8]9+', DP)
                            M0 = re.match(r'0+|[1-9]0+', DP)

                            # Check for chains of 9s
                            if M9:
                                C9 = len(M9.group(0))
                                if C9 > 4:
                                    R = round(R, len(DP) - 1)

                            # Check for chains of 0s
                            if M0:
                                C0 = len(M0.group(0))
                                if C0 > 4:
                                    R = round(R, len(DP) - 1)

                        if E != 0:
                            R = Seval(f'{R}e{E}')

                        else:
                            R = round(float(str(R).split('.')[0] + '.' +
                                            str(R).split('.')[-1]), 16)

                        if float(R).is_integer():
                            R = int(R)

                        S -= 1
                        if S:  # Complex
                            R1 = R
                            R = Seval(repr(J).strip('j'))

                        else:
                            break

                # except BaseException as e:
                #    print(e)

                if J is not None:
                    R = complex(R1, R)

                if isinstance(cls.object, Decimal):
                    R = Decimal(str(R))

                return R

            def periodic(cls, num):
                with Try:
                    if float(num).is_integer():
                        return Null

                    if 'e' in repr(num):
                        return Null

                    DP = repr(num).split('.')[-1]
                    TS = DP
                    P = 1

                    try:
                        while TS[-2] == '0':
                            TS = TS[:-2] + TS[-1]
                            P += 1
                    finally:
                        P += len(DP)
                    
                    if P < 15:
                        return Null

                    for PL in range(1, 9):
                        for SIDX in range(len(DP) - PL):
                            SDP = DP[SIDX:]
                            regex = re.compile(rf"(\d{{{PL}}})\1+")
                            match = regex.search(SDP)

                            if match:
                                RS = match.group(1)
                                RC = len(match.group(0)) // len(RS)
                                RD = SDP[match.end():]
                                if len(RD) <= len(RS):
                                    if Or((PL == 1 and RC >= 6),
                                          (PL == 2 and RC >= 5),
                                            (PL == 3 and RC >= 4),
                                            (PL == 4 and RC >= 3),
                                            (PL == 5 and RC >= 2),
                                            (PL >= 6 and RC >= 1)):
                                        if not RS.strip('0') == '':
                                            if len(RS) > 1 and (
                                                    RS.strip(RS[0]) == ''):
                                                break
                                            else:
                                                return RS

                return Null

        return Numeric(obj)

    for obj in plist(objs):
        S = numeric(obj)
        if S.type != type(S.value):  # Type correction for float(Xe+Y)
            S = numeric(S.value)
        R.append(S)

    return punit(R)


# FORMATTERS ==> Conformity Operators:
def plist(*vals: Any | Iterable[Any],
          ) -> List[Any]:
    """
    Plain List.

    Transforms iterable sets into a flat list; Recursive unpacking.
    Dictionaries are accounted for their values.

    :Examples:
        plist((1, 2), [3, 4], {5, 6})
            | [1, 2, 3, 4, 5, 6]

        plist({0: 10, 1: 20, 2: 40})
            | [10, 20, 40]

        plist({'A':10, 'B':15, 'C':20, 'D':{"X": 100, "Y": 200, "Z": 300}})
            | [10, 15, 20, 100, 200, 300]

    :Args:
        *vals: Any | Iterable[Any]
            | Data entries to be flattened.

    :Return:
        R: List[Any]
            | Flat list containing the data entries.
    """
    R: List[Any] = []

    for ele in vals:

        if isinstance(ele, dict):
            R.extend(plist(*ele.values()))

        elif isinstance(ele, (list, tuple, set)):
            R.extend(plist(*ele))

        else:
            R.append(ele)

    return R


def punit(*its: Iterable[Any],
          ) -> Any | Tuple[Any]:
    """
    Plain Units.

    Unpacks single units inside iterable sets.

    :Examples:
        punit([5], [3, 2], [[9]])
            | (5, [3, 2], 9)

        punit([1, 2], 3, (4,))
            | ([1, 2], 3, 4)

        punit([[7, 8]], {9})
            | ([7, 8], 9)

    :Args:
        *its: Iterable[Any]
            | Iterable sets.

    :Return:
        R: Any | Tuple[Any]
            | A single item or a tuple of items.
    """
    R: List[Any] = []

    for ele in its:

        if isinstance(ele, Iterable) and not isinstance(ele, (str, bytes)):

            if len(list(ele)) > 1:
                R.append(ele)
            else:
                R.extend(plist(ele))

        else:
            R.append(ele)

    match len(R):
        case 0:
            return None
        case 1:
            return R[0]
        case Z:
            return tuple(R)


def pround(*vals: Real | Iterable[Real | String],
           tol: String | Integer = 'auto',
           dcm: String | Integer = 'auto',
           ) -> Real | Iterable[Real] | None:
    """
    Plain Round.

    Numeric formatter; Evaluates numeric expressions;
    Less precise than `pnumber()`, but much faster.
    Removes floating point imprecision errors with great accuracy;
    Works well expressing repeating decimals.

    The 'tol' argument is used roughly for the precision of the output.
    It is designed to work 99.9% of the time, figuratively speaking,
    with a standard precision of up to 1e-12 when set to 'auto', as default.

    :Examples:
        pround([8.0, '0.1 * 3', '355/113', 'math.e'])
            | [8, 0.3, 3.1415929203539825, 2.718281828459045]

        pround(1/3, 10/33, 100/333, 1000/3333)
            | [0.333, 0.30303, 0.3003003003, 0.3000300030003]

        pround(0.1 ** 1e-12)
            | 0.9999999999977

        pround(0.1 ** 32) # Fails with 'auto' precision tolerance.
            | 0 # float(0.1 ** 32) is 1.0000000000000018e-32

        pround(0.1 ** 32, tol=32)
            | 1e-32

    :Args:
        *vals: Real | Iterable[Real | String]
            | Numbers to be formatted.

    :Kwargs:
        tol: String | Integer = 'auto'
            | Precision of the output;
            | It is recommended to follow the lowest decimal place.
            | i.e. tol=64 for a precision of up to 1e-64.

        dcm: String | Integer = 'auto'
            | Decimal places of the output;
            | It is involved in the rounding phase of the function.
            | 'auto' rounds repeating decimals up to 4 repetitions;
            | i.e. pnumber(1/3, dcm='auto') == 0.3333
            | dcm = ('all'|16|None) all end up with the same result.

    :Return:
        R: Real | Iterable[Real] | None
            | Formatted numbers, None if NaN.
    """
    R: List[Real] = []
    S: Real
    P: Bool
    I: Bool

    def RS(x, y): return round(x, y - max(repr(x)[
        repr(x).find('.') + 1:].rstrip('0').count(
        '0') // 4, repr(x)[repr(x).find(
            '.') + 1:].rstrip('9').count('9') // 4))

    def RT(x): return max(4, 16 - math.ceil(math.log(
        x, 96 if x < 1e-15 else
        48 if x < 1e-12 else
        24 if x < 1e-9 else
        12 if x < 1e-6 else
        6 if x < 1e-3 else
        3)))

    for val in plist(vals):

        with Try:
            P = False
            I = False
            num = Seval(str(val))

            if float(num).is_integer():
                R.append(int(num))
                continue

            if tol == 'auto' or not tol or not isinstance(tol, int):
                tol = RT(abs(num))

            else:
                tol += 3  # Account for rounding

            # CHECK 1: Float imprecision
            num = RS(num, tol)

            # https://stackoverflow.com/a/38847691/26469850
            dnum = format(decimal.Context(prec=32).create_decimal(
                repr(num)), 'f')

            # CHECK 2: Float imprecision
            while re.compile(  # re is some black magic, I swear. LLM used.
                    r'^-?\d+\.\d*?[1-9](0{5,})([1-9]{1,2})$').search(dnum):
                dnum = dnum[:-1]
                I = True

            for length in range(1, len(dnum) // 4 + 1):
                for start in range(len(dnum) - length * 4):
                    period = dnum[start:start + length]
                    if period * 4 == dnum[start:start + length * 4] and (
                            period != '0' * length):
                        S = round(float(dnum), len(
                            dnum[:start] or '') + (len(period) * 3) - 1) if (
                                dcm == 'auto') else float(dnum) if (
                                    dcm == 'all') else round(float(dnum), dcm)
                        if not math.isclose(S, int(S),
                                            rel_tol=1e-15,
                                            abs_tol=1e-15):
                            P = True
                        else:
                            S = int(S)
                        break
                else:  # nobreak
                    continue
                break
            else:  # nobreak
                S = float(dnum)
                if S.is_integer():
                    S = int(S)

            if not math.isclose(
                    Decimal(S), Decimal(dnum), rel_tol=1e-15,
                    abs_tol=1e-15) and not I and not P:
                S = float(num)

            R.append(S)

    return punit(R)


def pdecimals(*nums: Real | Iterable[Real | String],
              ) -> Integer:
    """
    Plain Decimals.

    Identifies the highest number of decimal places in a set.

    If the number has a repeating period (detected by `pt.pnumber()`), the
    return value will be `float('inf')`, even if the Python representation of
    the `float(num)` is limited to 16 decimal places.

    :Example:
        pdecimals(1.23, 4.5678, 3.1, 5.67890)
            | 4

        pdecimals(1/3)
            | inf

        pdecimals(math.pi)
            | 15

    :Args:
        [*]nums: Real | Iterable[Real | String]
            | Numbers to be formatted.

    :Returns:
        R: Integer
            | Highest quantity of decimal places found.
    """
    R: Integer = 0

    for num in plist(nums):
        num = pnumber(num)
        etol = 'auto'
        if num.period != None:
            return float('inf')
        if 'e-' in str(num):
            etol = int(num.string.split('e-')[-1])
        prd = str(pround(abs(num) - math.floor(abs(num)), tol=etol))
        num = pround(prd, tol=etol)
        if Seval(prd) == 0:
            continue
        if 'e-' in prd:
            enot = int(prd.split('e-')[-1])
            prd = f"{num:.{enot}f}"
        if '.' in prd:
            R = max(R, len(prd.split('.')[1]))

    return R


def pstring(*objs: Any | Iterable[Any],
            sep: String = ', ',
            ) -> String:
    """
    Plain String.

    More comprehensible 'str()' operator; concatenates elements of iterables.

    :Examples:
        pstring({0: 'a', 1: 'b', 2: 'c'})
            | '0: a, 1: b, 2: c'

        pstring([1, 2, 3], (4, 5), {6, 7})
            | '1, 2, 3, 4, 5, 6, 7'

        pstring('Hello', ['world', '!'], sep = ' ')
            | 'Hello world !'

    :Args:
        *objs: Any | Iterable[Any]
            | Objects to be converted to string.

    :Kwargs:
        sep: String = ', '
            | Separator between elements in the final string.

    :Return:
        R: String
            | Single string containing the concatenated elements.
    """
    R: List[String] = []

    for obj in objs:

        T = pistype(obj,
                    dict,                 # T[0]
                    (list, tuple, set),   # T[1]
                    type,                 # T[2]
                    )

        if T[0]:
            R.extend(f'{k}: {v}' for k, v in obj.items())

        elif T[1]:
            R.extend(map(str, obj))

        elif T[2]:
            R.append(obj.__name__)

        else:
            R.append(str(obj))

    return sep.join(R)


def pistype(obj: Any,
            *types: Type,
            ) -> Bool | Tuple[Bool]:
    """
    Plain Type Check.

    Checks if the object is an instance of the provided types.

    :Examples:
        pistype('Hello', String, Iterable, Set)
            | (True, True, False)

        pistype([1, 2, 3], List, Tuple, Iterable)
            | (True, False, True)

        pistype(42.0, Number, Integer, Float)
            | (True, False, True)

    :Args:
        obj: Any
            | Object to be checked against.

        *types: Type
            | Types to compare using isinstance(obj, type).

    :Return:
        R: Bool | Tuple[Bool]
            | Sequence of Booleans according to the checks.
    """
    return punit(tuple(isinstance(obj, t) for t in types))


def prange(*args: Real,
           start: Real = None,
           stop: Real = None,
           step: Real = None,
           type: String = None,
           ) -> Iterable[Real]:
    """
    Plain Range.

    Simulates the 'range()' function from Python 2.x.

    Instead of a *range* object, returns a plain *Iterable* of specified type.

    Stop argument is the de-facto stop, being the last value of list.

    Args functionality is the same as standard 'range()' built-in function.

    :Example:
        prange(5)
            | [0, 1, 2, 3, 4, 5]

        prange(5, 2.5, 0.5, 'tuple')
            | (5, 4.5, 4, 3.5, 3, 2.5)

        prange(0, 15, 4, 'dict')
            | {0: 0, 1: 4, 2: 8, 3: 12}

    :Args:
        *args: Real
            Functionality varies according to arguments:
                - A single parameter determines the `stop`; with `start` of 1.
                - Two parameters determines `start` and `stop`; with `step` of 1.
                - Three parameters determines `start`, `stop` and `step`; returning a `list`.
                - Four parameters determines `start`, `stop`, `step` and `type`

    :Kwargs:
        start: Real = None
            | Start value of the iterable.

        stop: Real = None
            | Stop value of the iterable.

        step: Real = None
            | Step value of the iterable.

        type: String = None
            | Return type ('list', 'tuple', 'set', 'dict').


    :Returns:
        R: Iterable[Real] = Iterable (defined in 'get') containing the range.
    """
    match len(args):

        case 1:
            stop = stop or args[0]
            start = 0
            step = 1
            type = 'list'

        case 2:
            start = start or args[0]
            stop = stop or args[1]
            step = 1
            type = 'list'

        case 3:
            start = start or args[0]
            stop = stop or args[1]
            step = step or args[2]
            type = 'list'

        case 4:
            start = start or args[0]
            stop = stop or args[1]
            step = step or args[2]
            type = type or args[3]

        case Z:
            raise TypeError(f"prange expected at most 4 arguments, got {Z}")

    R: Iterable[Real] = []
    C: Real = pnumber(start)

    if step == 0:
        raise ValueError('prange() step must not be zero')

    if start <= stop:

        while C <= stop:
            R.append(C)
            C += abs(step)

    else:

        while C >= stop:
            R.append(C)
            C -= abs(step)
    
    if math.isclose(R[-1], stop):
        R = R[:-1] + [stop]
    
    if R[-1] != stop:
        R.append(stop)

    match type.lower():

        case 'list':
            return R

        case 'tuple':
            return tuple(R)

        case 'set':
            return set(R)

        case 'dict' | 'dictionary':
            return dict(enumerate(R))


def pinterval(*args: Real,
              divs: Real = None,
              start: Real = None,
              stop: Real = None,
              type: String = None,
              ) -> Iterable[Real]:
    """
    Plain Interval.

    Generates a list of numeric elements equidistant between them,
    from start to stop.

    :Examples:
        pinterval(5)
            | [0, 25, 50, 75, 100]

        pinterval(3, 5)
            | [0, 2.5, 5]

        pinterval(5, 10, 0, 'dict')
            | {0: 10, 1: 7.5, 2: 5, 3: 2.5, 4: 0}

    :Args:
        *args: Real
            | Can contain up to four positional arguments:
                - One argument: divs;
                    List of [0, 0±n1, 0±n2, (...), 100] with 'divs' elements.
                - Two arguments: divs and stop;
                    List of [0, 0±n1, 0±n2, (...), stop] with 'divs' elements.
                - Three arguments: divs, start and stop;
                    List of [start, start±n1, (...), stop] with 'divs' elems.
                - Four arguments: divs, start, stop and type.
                    Iterable of type(start, (...), stop) with 'divs' elements.

    :Kwargs:
        divs: Real = None
            | Number of elements in the returned Iterable.

        start: Real = None
            | Start value of the interval (default is 0).

        stop: Real = None
            | Stop value of the interval.

        type: String = None
            | Return type ('list', 'tuple', 'set', 'dict').

    :Return:
        R: Iterable[Real]
            | List of numeric values with equidistant intervals.
    """

    match len(args):

        case 1:
            start = 0
            stop = 100
            divs = pnumber(stop / max(args[0] - 1, 1))
            type = 'list'

        case 2:
            start = 0
            stop = stop or args[1]
            divs = pnumber(stop / max(args[0] - 1, 1))
            type = 'list'

        case 3:
            start = start or args[1]
            stop = stop or args[2]
            divs = pnumber((stop - start) / max(args[0] - 1, 1))
            type = 'list'

        case 4:
            start = start or args[1]
            stop = stop or args[2]
            divs = pnumber((stop - start) / max(args[0] - 1, 1))
            type = type or args[3]

        case Z:
            raise TypeError(f"pinterval expected at most 4 arguments, got {Z}")

    return prange(start, stop, divs, type)


def psequence(*nums: Real | Iterable[Real],
              abs_lim: Real = None,
              rel_lim: Real = 10e3,
              ) -> Chain[Real]:
    """
    Plain Sequence.

    Generates a numerical sequence based on the provided numbers or patterns.

    It supports the use of ellipsis (`...`) to denote the continuation
    of the sequence with a defined step or to an optional limit.

    :Args:
        *nums: Real | Iterable[Real]
            | The numbers or patterns used to generate the sequence.
            | Ellipsis (`...`) can be used to sign continuation of sequence.

    :Kwargs:
        abs_lim: Real = None
            | The absolute limit for the sequence, if provided.

        rel_lim: Real = 10e3
            | The relative limit, as a multiplier to the last expressed num.

    :Returns:
        R: Chain[Real]
            | A chain of numbers representing the generated sequence.

    :Example:
        psequence(1, 2, 3, ..., 10)
            | Generates the sequence equivalent to (1, 2, ..., 9, 10).

        psequence(1, 3, 5, ..., abs_lim=150)
            | Generates the sequence equivalent to (1, 3, ..., 147, 149).

        psequence(0.1)
            | Generates the sequence equiv. to (0.1, 0.2, ..., 999.9, 1000).

    :Notes:
        - If an ellipsis (`...`) is used, the function will infer the step
          from the preceding numbers in the sequence.
        - If `abs_lim` is provided, the sequence will stop when it reaches
          or exceeds this limit.
        - If `rel_lim` is provided, it will be used to calculate the maximum
          limit based on the last number in the sequence before the ellipsis.
        - The sequence continues either until the absolute
          or relative limit is met.
    """
    L: List[Real] = []
    N: List[Real | ...] = plist(nums)
    S: Real = None

    if len(N) == 0:
        return itertools.chain.from_iterable(L)

    if len(N) == 1:
        return psequence(N[0], ...,
                         abs_lim=abs_lim,
                         rel_lim=rel_lim,
                         )

    elif N[-1] != ...:
        return psequence(N[:-1],
                         abs_lim=abs_lim or N[-1],
                         rel_lim=rel_lim,
                         )

    if abs_lim is not None:
        limit = pround(abs_lim)

    else:
        if rel_lim is not None:
            limit = pround(N[-2] * rel_lim) if N[-1] == ... else pround(
                N[-1] * rel_lim) if N[-1] == ... else N[-1]

        else:
            limit = float('inf')

    rnd = 0
    nums = [x for x in N if x != ...]
    nums.append(limit)

    for i in nums:
        try:
            if 'e-' in repr(i):
                rnd = max(rnd, int((repr(i).split('.')[-1].split('e-')[-1])
                                   .lstrip('0')))
            else:
                rnd = max(rnd, len(repr(i).split('.')[-1]))
        except BaseException:
            continue

    rnd = int(rnd)

    for i, num in enumerate(N):
        if num == ...:
            if i == 0:
                raise ValueError(
                    "Ellipsis cannot be the first element of a sequence.")

            start = N[i - 1]
            if S is None and i >= 2:
                S = start - N[i - 2]

            if i == len(N) - 1:
                if S is None:
                    S = start
                L.append(pround(round(x, rnd)) for x in itertools.takewhile(
                    lambda x: x >= limit if S < 0 else (
                        x <= limit or abs(x - limit) < S / 10),
                    itertools.count(start + S, S)))
            else:
                end = N[i + 1]
                if S is None:
                    S = end - start
                L.append(pround(round(x, rnd)) for x in itertools.takewhile(
                    lambda x: x <= limit if S < 0 else (
                        x >= limit or abs(x - limit) < S / 10),
                    itertools.count(start + S, S)))
        else:
            L.append([pround(num)])

    return itertools.chain.from_iterable(L)


def pindex(target: Any,
           *its: Iterable[Any],
           ) -> Integer | None | Tuple[Integer | None]:
    """
    Plain Index.

    Returns the index of the first occurrence of 'target' in 'its'.

    :Examples:
        pindex(True, (False, False, True))
            | 2

        pindex(5, range(10))
            | 5

        pindex(1, (False, False, True), ['a', 'b', 'c'], range(10))
            | (2, None, 1)

    :Args:
        target: Any
            | Value to search for in the provided iterables.

        *its: Iterable[Any]
            | One or more iterables to be checked for 'target'.

    :Return:
        R: Integer | None | Tuple[Integer | None]
            | Index of the first 'target' occurrence into provided iterables.
    """
    R: List[Integer | None] = []

    for it in its:
        R.append(next((i for i, e in enumerate(it) if e == target), None))

    return punit(tuple(R))


def pminmax(*vals: Real | Iterable[Real],
            ) -> Container[String: Real]:
    """
    Plain MinMax.

    Returns the minimum and maximum values from a set of numbers.

    :Examples:
        pminmax([5, 2, -8, '15*2'])
            | {'min': -8, 'max': 30}

        pminmax([5, 2, -8, '15*2']).min
            | -8

        pminmax(1, -2, ['1.5 * 2'], math.pi)[1][1]
            | 3.141592653589793

    :Args:
        *vals: Real | Iterable[Real]
            | Objects to be counted.

    :Return:
        R: Container[String: Real]
            | A Container, derived from dict, containing min & max values.
    """
    R: Container[String: Real] = Container(
        min=min(plist(pnumber(vals))),
        max=max(plist(pnumber(vals))))

    return R


def plen(*iters: Any | Iterable[Any],
         ) -> Container[String: Integer]:
    """
    Plain Length.

    Returns the minimum and maximum sizes of given iterables.

    :Examples:
        plen([1, 2, 3], (4, 5), {6})
            | {'min': 1, 'max': 3}

        plen([1, 2, 3, [4, 5], 6], ("ABCDEFGHIJ", "XYZ"), {}).min
            | 0

        plen({0: 1, 1: -2, 2: 4, 3: -8, 4: 16, 5: 32}).max
            | 6

    :Args:
        *iters: Iterable[Any]
            | Objects to be counted.

    :Return:
        R: Container[String: Integer]
            | A Container , derived from dict, containing min & max lengths.
    """
    R: List[Integer] = []

    if not iters:
        return (0, 0)

    for it in iters:

        try:
            R.append(len(it))

        except TypeError:
            R.append(1)

    return pminmax(R)


def pabs(*nums: Real | Iterable[Real | String],
         ) -> Container[String: Real]:
    """
    Plain Absolutes.

    Identifies the lowest and highest absolute numbers from given sets.
    Returns a Container with the min, max, original min, original max values.

    :Examples:
        x = pabs([5, 8, -2, '15*2'])
            | x == {'min':2, 'max':30, 'ogmin':-2, 'ogmax': 30}
            | x.min == 2
            | x.ogmin == -2
            | x.max == x.ogmax == 30

        y = pabs(-1, -2, ['1.5 * 2'], math.pi)
            | y['min'] == 1
            | y['ogmin'] == -2
            | y['max'] == 3.141592653589793

        zmin, zmax, ztruemin, ztruemax = pabs(prange(-10, 0, 1))
            | zmin == 0
            | zmax == 10
            | ztruemin == -10
            | ztruemax == 0

    :Args:
        *nums: Real | Iterable[Real | String]
            | Objects to be counted.

    :Return:
        R: Container[String: Real]
            | Dict-subclass with min, max, original min and original max.
    """
    R: Container[String: Real]
    nums = pnumber(plist(nums))

    return Container(min=min([abs(num) for num in nums]),
                     max=max([abs(num) for num in nums]),
                     ogmin=min([num for num in nums]),
                     ogmax=max([num for num in nums]),
                     )


def psum(*nums: Real | Iterable[Real | String],
         ) -> Real:
    """
    Plain Sum.

    Returns the sum of possible numbers from given sets.

    :Examples:
        psum([5, 2, -8, '15*2'])
            | 29

        psum(prange(-10, 0))
            | -55

        psum(Container(John=2.55, Maria=3.14, Paul=1.75))
            | 7.44

    :Args:
        *nums: Real | Iterable[Real | String]
            | Objects to be counted.

    :Return:
        R: Real
            | Sum of numbers.
    """
    R: Real = 0
    for num in pnumber(nums):
        with Try:
            R += num

    return pnumber(R)


def pimport(libs: String,
            funs: String = None
            ) -> Module | Object | Tuple[Module | Object]:
    """
    Plain Import.

    Helper function for local scope importation.

    :Examples:
        calc = pimport('math')
            | Allocates 'calc' as alias to 'math' module.

        pi, log = pimport('math','pi, log')
            | Allocates to variables the imported objects (math.pi, math.log).

    :Args:
        libs: String
            | Modules to import; separated by ','.

        funs: String
            | (None) Objects to import; separated by ','.

    :Return:
        R: Module | Object | Tuple[Module | Object]
            | Imported modules or objects.
    """
    modules: String = libs.split(",")
    imports: Set = {}
    context: Dictionary = pframe(2).f_locals

    for mod in modules:
        mod = mod.strip()

        try:
            imod = importlib.import_module(mod)

            if funs:
                fun = funs.split(",")

                for fn in fun:
                    fn = fn.strip()

                    try:
                        imports[fn] = getattr(imod, fn)

                    except AttributeError:
                        pass

            else:
                imports[mod] = imod

        except ModuleNotFoundError:
            pass

    for k, v in imports.items():
        context[k] = v

    return (
        tuple(imports.values())
        if len(imports) > 1
        else next(iter(imports.values()), None)
    )


def pframe(depth: Integer = 1,
           outer: Bool = False,
           ) -> Frame:
    """
    Plain Frame.

    Helper function for getting the frame information in specified depth.

    :Examples:
        x = pframe()
            | x.filename == 'PlainTools.py'
            | x.lineno == 42
            | x.name == 'pframe'

    :Args:
        depth: Integer = 1
            | (Default: 1) How many frames to go in;
            : Note that this is in reverse order, so a depth=2
            inspects the currentframe up until currentframe()[-2]

    :Kwargs:
        outer: Bool = False
            | Determines if the Frame is get from inspect.getouterframes()

    :Return:
        R: FrameInfo
            | Frame object.
    """
    if outer:
        return inspect.getouterframes(inspect.currentframe())[-depth].frame

    R: Frame = inspect.currentframe()
    i: Integer = 0

    while R.f_back is not None:
        R = R.f_back
        i += 1

        if i >= depth:
            break

    return R


# DEBUG | CONSOLE ==> End Prompt, Traceback, sys.stdout etc.
def clear(*buffer: Any,
          ) -> None:
    """
    Clear Screen.

    :Rationale:
        Simple command to clear the console feed.
    """
    sys, nm = pimport("os", "system,name")
    sys("cls" if nm == "nt" else "clear")


def debug(*buffer: Any,  # Buffer
          ) -> List[String] | None:
    """
    Debug Traceback.

    :Example:
        - Try: (...)
        - Except: printnl(*debug())

    :Rationale:
        Returns the traceback, if any.
    """
    trace = traceback.format_exc()
    call = pframe(2)

    if len(trace.splitlines()) <= 1:
        return  # No traceback.

    trace = trace.splitlines()

    trace[0] += " → " + trace[2].strip()

    trace.pop(2)

    for i in range(3, len(trace) - 1):
        trace[i] = "  " + trace[i]

    trace[-1] = "Er " + trace[-1]
    Logging(trace)

    return trace


def eof(*buffer: Any,  # Buffer
        ) -> SystemExit:
    """
    End of File.

    :Rationale:
        Logs into a .log file, waits for user input, and then exits the system.
    """
    debug()
    skip()
    printc('[!-END-OF-FILE-!]', fill='=')
    skip()

    if Logging.get:
        Logging.show.flush

    input()
    exit()


def deepframe(*buffer: Any,  # Buffer
              ) -> None:
    """
    Deep Frame.

    :Rationale:
        Prints the full depth of the current path and the frame stack.
    """
    Sar = inspect.getouterframes(inspect.currentframe())
    print('\n[!-DEEPFRAME-!]')
    print('\n[|-ABSPATH-|] -> sys.argv [i]')
    i = 0

    while True:
        try:
            print(f'[{i}] ->', os.path.abspath(Sar[i]))
            i += 1

        except BaseException:
            break

    skip()
    print('[|-ABSPATH-|] -> inspect.getfile.stack()[j].frame')
    j = 0

    while True:
        try:
            print(f'[{j}] ->', os.path.abspath(inspect.getfile(
                inspect.stack()[j].frame)))
            j += 1

        except BaseException:
            break

    skip()


def printnl(*args, **kwargs):
    """
    New Line Print.

    :Rationale:
        Prints the input with a new line after each prompt.
    """
    for arg in args:
        print(arg, **kwargs)


def printc(*args, fill=' ', **kwargs):
    """
    Centered Print.

    :Rationale:
        Prints the input centered on the window.
    """
    for arg in args:
        print(str(arg).center(shutil.get_terminal_size(
        ).columns, fill), **kwargs)


def skip(n=1, *args, **kwargs) -> None:
    """
    Line Skip.

    Prints into the console 'n' times; Defaults to a 1 line skip.
    """
    for i in range(n):
        print(*args, **kwargs)


def evinput(*args, **kwargs) -> Any:
    """
    Evaluated Input.

    Uses a Safe Eval on the given input and returns it.
    """
    R = input(*args, **kwargs)
    try:
        R = Seval(R) or R
    finally:
        return R


def let(**kwargs) -> Container[Any: Any]:
    """
    Let 'Statement'.

    Note: The 'let()' function is unusable inside function definition scopes;
    It is neither a bug nor fixable, but a limitation of the Python language.

    Assigns and evaluates multiple variables in a single function call.

    Keep in mind that real assignment happens after the function call ends;
    Doing 'let(x=5, y=10, z=x+y)' raises 'NameError: name 'x' is not defined';
    But doing 'let(x=5, y=10), let(z=x+y)' works just fine.

    :Examples:
        let(x=5, y=10, z=math.pi)
            | (5, 10, 3.141592653589793)
            | x = 5
            | y = 10
            | z = 3.141592653589793

        let(w=Seval('15 ** 5 / 2'))
            | w = 379687.5

    :Kwargs:
        **kwargs: Any
            | Direct assignments to given kwarg variables.

    :Return:
        R: Container[Any: Any]
            | A Container with the relationed objects assigned.
    """
    R: Container[Any: Any] = Container(kwargs)
    C: Frame = pframe(2)

    for k, v in R:
        exec(f"{k} = {repr(v)}",
             C.f_globals,
             C.f_locals,
             )

    return R


def const(**kwargs) -> Container[Constant: Any]:
    """
    Constant 'Statement'.

    Note: The 'const()' function is unusable in function definition scopes;
    It is neither a bug nor fixable, but a limitation of the Python language.

    Assigns and evaluates multiple constant variables in a function call.
    Returns Constant objects, being immutable by nature.

    Keep in mind that real assignmenet happens after the function call ends;
    Doing 'const(x=5, z=x+5)' raises 'NameError: name 'x' is not defined';
    But doing 'const(x=5), const(z=x+5)' works just fine.


    :Examples:
        const(x=2.5, y=3.5)
            | (2.5, 3.5)
            | x == Constant(2.5)
            | y == Constant(3.5)

        const(z=[0, 1, 1, 2, 3, 5, 8, 13])
            | z == Constant([0, 1, 1, 2, 3, 5, 8, 13])

    :Kwargs:
        **kwargs: dict
            | Additional constants to assign in the current context.

    :Return:
        R: Container[Constant: Any]
            | A Container with the relationed objects assigned as Constants.
    """
    R: Container[Any: Any] = Container(kwargs)
    C: Frame = pframe(2)

    C.f_locals.update((kwarg, Constant(kwargs[kwarg])) for kwarg in kwargs)

    return R


def timeout(secs: Real,
            func: Callable,
            *args: Any,
            **kwargs: Any,
            ) -> Any | Err:
    """
    Timeout.

    Runs a function in a separate proccess with a time limit;
    Raises an exception if it exceeds given limit in seconds.

    :Examples:
        timeout(5, long_running_function, arg1, arg2)
            | Executes long_running_function with a 5-second limit.

    :Args:
        secs: Real
            | Time limit in seconds.

        func: Callable
            | Function to execute.

        *args: Any
            | Positional arguments to pass to the function.

        **kwargs: Any
            | Keyword arguments to pass to the function.

    :Return:
        R: Any | Err
            | The result of the function, or an exception if timed out.
    """
    try:
        q = multiprocessing.Queue()
        t = Time
        proc = multiprocessing.Process(
            target=qfunc,
            args=(func, q, args, kwargs)
        )

        t.now
        proc.start()
        proc.join(timeout=secs)
        if proc.is_alive():
            proc.terminate()
            raise TimeoutError(f'[TIMEOUT:FAIL] - {t.now}s')
        else:
            return q.get()

    except BaseException as e:
        return e


def qfunc(func, queue, args, kwargs) -> None:
    try:
        queue.put(func(*args, **kwargs))

    except BaseException as e:
        queue.put(e)


def loop(times: Integer = 0,
         escape: Exception | Tuple[Exception, ...] = KeyboardInterrupt,
         loopif: Function | Bool = True,
         show: Bool = False,
         nl: Bool = False
         ) -> Decorator:
    """
    Loop Decorator.

    A decorator that repeatedly executes the function based on
    specified conditions.

    It allows for control over the number of iterations,
    conditional execution, and exception handling within the loop.

    Exceptions raised by the function do not inherently stop the loop
    unless their type is specified in the escape parameter. However,
    the KeyboardInterrupt exception is guaranteed to always be caught
    and interrupt the loop execution.

    :Examples:
        @loop(times=3)
        def my_function(x):
            print(f"Value: {x}")
        | This will print the value of `x` three times at 'my_function()'.

        @loop(loopif=lambda: some_condition())
        def my_function(x):
            print(f"Value: {x}")
        | This will execute `my_function` as long as `some_condition()`
        : returns True.

        @loop(escape=KeyboardInterrupt)
        def my_function(x):
            print(f"Processing {x}")
        | This will execute `my_function` in a loop until a
        : `KeyboardInterrupt` exception is raised.

        @loop(times=5, show=True)
        def example_function(x):
            print(x)
        | This will run `example_function` 5 times, printing the iteration
        : details each time.

    :Args:
        times: Integer = 0
            | The number of times to execute the decorated function.
            | If set to 0, the loop will run indefinitely unless broken out.
            | Default is 0.

        escape: Exception | Tuple[Exception, ...] = KeyboardInterrupt
            | Exception(s) that, if raised, will stop the loop.
            | Default is KeyboardInterrupt (guaranteed even if changed).

        loopif: Function | Bool = True
            | A condition that, if evaluated to False, will break the loop.
            | It can be a Lambda type with out-scope parameters or conditions.
            | Default is True.

        show: Bool = False
            | If True, prints the function name, arguments, and iteration.
            | Default is False.

        nl: Bool = False
            | If True, inserts a newline after each iteration.
            | Default is False.

    :Returns:
        Decorator
            | A decorator that wraps the provided function.
    """
    if times <= 0:
        times = float('inf')

    if KeyboardInterrupt not in plist(escape):
        escape = (escape, KeyboardInterrupt)

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            iteration = 0

            while True:
                if times and iteration >= times:
                    break

                if loopif:
                    if callable(loopif):
                        if not loopif(*args, **kwargs):
                            break
                    elif isinstance(loopif, bool):
                        if not loopif:
                            break

                result = None

                try:
                    if show:
                        print(f"@Loop [T{iteration + 1}]:",
                              f"Fn {func.__name__}({args}, {kwargs})" if (
                            args and kwargs) else (
                            f"Fn {func.__name__}({args})"
                            if (args and not kwargs) else (
                                f"Fn {func.__name__}({kwargs})"
                                if (not args and kwargs) else (
                                    f"Fn {func.__name__}()"
                                )
                            )
                        ),
                        )
                    try:
                        result = func(*args, **kwargs)

                    except escape as e:
                        raise e

                    except BaseException as e:
                        print(f"@Loop [!-FAIL-!]: {e.__class__.__name__}")

                    # Show verbose output if enabled

                    # Increment iteration counter
                    iteration += 1

                    # Insert newline if enabled
                    if nl:
                        print()

                except escape as e:
                    if show:
                        print(
                            f"@Loop [!-HALTED-!]: {e.__class__.__name__}")
                        if str(e):
                            print(e)
                    break

                if not times and not loopif:
                    break

            return result

        return wrapper

    return decorator


def arithmetic(cls):
    def operate(op):
        @functools.wraps(op)
        def wrapper(self, other=None):
            val = self.value

            if isinstance(other, cls):
                other = other.value

            if isinstance(val, Iterable) and not isinstance(val, (
                    String, Bytes)):
                val = type(val)(op(v, other) for v in val)
            else:
                try:
                    if other is not None:
                        val = op(val, other)
                    else:
                        val = op(val, Null)

                except TypeError:
                    val = op(val)

            return cls(val)

        return wrapper

    for opn, opf in {
        '__add__': operator.add,
        '__sub__': operator.sub,
        '__mul__': operator.mul,
        '__truediv__': operator.truediv,
        '__floordiv__': operator.floordiv,
        '__mod__': operator.mod,
        '__pow__': operator.pow,
        '__eq__': operator.eq,
        '__ne__': operator.ne,
        '__lt__': operator.lt,
        '__le__': operator.le,
        '__gt__': operator.gt,
        '__ge__': operator.ge,
        '__and__': operator.and_,
        '__or__': operator.or_,
        '__xor__': operator.xor,
        '__rshift__': operator.rshift,
        '__lshift__': operator.lshift,
        '__neg__': operator.neg,
        '__pos__': operator.pos,
        '__abs__': operator.abs,
        '__invert__': operator.invert,
    }.items():
        setattr(cls, opn, operate(opf))

    def __getattr__(cls, item):
        if item in dir(cls):
            return getattr(cls, item)
        if item in dir(cls.value):
            return getattr(cls.value, item)
        for typ in (Decimal, Fraction, float, int):
            if item in dir(typ):
                return getattr(typ(cls.value), item)
        raise AttributeError(
            f"'{cls.__class__.__name__}' | '{cls.value.__class__.__name__}'" + (
                f" objects have no attribute '{item}'"))

    setattr(cls, '__getattr__', __getattr__)

    def __getattribute__(self, name):
        try:
            return super(cls, self).__getattribute__(name)
        except (TypeError, ValueError) as e:
            value = super(cls, self).__getattribute__('value')
            return getattr(value, name)

    setattr(cls, '__getattribute__', __getattribute__)

    setattr(cls, '__complex__', lambda cls: complex(cls.value))

    setattr(cls, '__float__', lambda cls: float(cls.value))

    setattr(cls, '__int__', lambda cls: int(cls.value))

    setattr(cls, '__round__', lambda cls, ndigits=0: round(
        cls.value, attempt(0, int, ndigits)))

    return cls


def showcall(func: Function) -> Function:
    """
    Show Call Information.

    This decorator outputs detailed information about the function
    call, including the line number, function name, arguments, return
    value or error, and execution time. It is useful for debugging and
    monitoring function execution.

    :Example:
        @showcall
        def my_function(x, y):
            return x + y
        | my_function(3, 4)
        |
        | [!-CALL-!]
        | Ln 10
        | Fn my_function
        | A* (3, 4)
        | K* {}
        |
        | [!-CALL-!]
        | R* 7
        | Tm 0.0001s
    """
    def wrapper(*args, **kwargs) -> Any:
        timer = TIME()
        line = inspect.getframeinfo(inspect.stack()[-1][0]).lineno
        with Try:
            call_info = ("[!-CALL-!]",
                         f"Ln {line}",
                         f"Fn {func.__name__}",
                         f"A* {args}",
                         f"K* {kwargs}")

            print(*call_info, sep='\n')

            try:
                result = func(*args, **kwargs)
            except BaseException as e:
                result = f"[!-ERROR-!]\nEr {e.__class__.__name__} \n" + (
                    f"As {e}"
                )

            call_info += (f"R* {result}",
                          f"Tm {timer.time}s")

            print(*call_info[5:], sep='\n')

        return result

    return wrapper


def moduleview(module: Module | String) -> Container:
    """
    Module View.

    Returns a Container of a module's attributes and values.

    Note that, as the return type is a Container, you can do such as:
        | calc = moduleview('math')
        | calc.pi # the exact same as math.pi

    :Args:
        module: Module | String
            | Module to be viewed. If String, its imported as a module object.

    :Return:
        R: Container
            | View of the module as k:v pairs.
    """
    R: Container = {}
    if isinstance(module, str):
        module = pimport(module)
    RL = dir(module)

    for i, j in enumerate(RL):
        R[j] = getattr(module, j)

    return Container(R)


def attempt(fallback: Any, operator: Any, *args, **kwargs) -> Any:
    """
    Attempt Operator

    Attempts to execute operator(*args, **kwargs), 
    returns 'fallback' if any exceptions occur.
    """
    with Try:
        return operator(*args, **kwargs)
    return fallback


# OPERATOR CLASSES ==> Instantiable Operators:
class TIME:
    """
    Execution Timer.

    A running timer that starts immediately when instantiated.

    :Example:
        X = TIME()  # Starts 'X' as a timer.
        with X:     # Starts a timed context with 'X'; prints time on exit.
        X.show      # Prints the current time in string format.

    :Args:
        add: Float = 0.0
            | Time to add to the timer.
        std: String = 'now'
            | Initial standard mode ('now', 'lap', or 'epoch').

    :Methods:
        .mode(std: String = '') -> Class
            | Changes the standard mode of the timer.

        .now -> Float
            | Returns the time since the last call.

        .lap -> Float
            | Returns the current time.

        .reset -> Class
            | Resets the timer.

        .string -> String
            | Returns the time as a string.

        .show -> String
            | Prints the current time in string format.

        .epoch -> List[Float]
            | Returns recorded times.

    :Instances:
        Time = TIME(std='now')
            | Timer that returns the time since the last call.

        Runtime = TIME(std='lap')
            | Timer that returns the total elapsed time.

        Crono = TIME(std='epoch')
            | Timer that returns the entire history of recorded times.

    :Returns:
        R: Float | List[Float]
            | Time in seconds.milliseconds (e.g., 1.234s).
    """
    def __init__(cls: Self,
                 add: Float = 0.0,
                 std: String = 'now',
                 ) -> Class:
        cls.timer = time.time()
        cls.travel = [0.0]

        match std:

            case 'now' | 'lap' | 'epoch':
                cls.std = std

            case Z:
                cls.std = 'now'

        cls(add)  # Quickstart; Inicia o cronômetro ao instanciar.

    def __call__(cls: Self,
                 add: Float = 0.0,
                 std: String = '',
                 ) -> Class:
        if std:
            cls.std = std
        cls.travel.append((time.time() - cls.timer) + add)
        return cls

    def __round__(cls: Self,
                  ndigits: Integer = 3,
                  ) -> Float:
        return pnumber(round(cls.travel[-1], ndigits))

    def __enter__(cls: Self
                  ) -> Class:
        cls.__init__()
        return cls

    def __exit__(cls: Self,
                 exc_type: BaseException,
                 exc_val: Exception,
                 exc_tb: Traceback,
                 ) -> String:
        debug()
        return cls.show

    @classmethod
    def mode(cls: Self,
             std: String = '',
             ) -> Class:
        match std:

            case 'now' | 'lap' | 'epoch':
                newstd = std

            case Z:
                print('[‼-ERROR-‼] -> %s' %
                      'TIME STANDARD INCOMPATIBLE: %s' % std)
                newstd = 'now'

        cls.std = newstd
        return cls

    @property
    def now(cls: Self,
            ) -> Float:
        cls.travel.append((time.time() - cls.timer))
        return pnumber(round(cls.travel[-1] - cls.travel[-2], 3))

    @property
    def lap(cls: Self,
            ) -> Float:
        cls.travel.append((time.time() - cls.timer))
        return pnumber(round(cls.travel[-1], 3))

    @property
    def epoch(cls: Self,
              ) -> List[Float]:
        return cls.travel

    @property
    def time(cls: Self,
             ) -> Float | List[Float]:

        match cls.std:

            case 'now':
                return cls.now

            case 'lap':
                return cls.lap

            case 'epoch':
                return cls.epoch

    @property
    def reset(cls: Self,
              ) -> Class:
        cls.timer = time.time()
        cls.travel = [0.0]
        return cls

    @property
    def string(cls: Self,
               ) -> String:
        match cls.std:

            case 'now':
                showtime = '[Time] -> %ss' % cls.now

            case 'lap':
                showtime = '[Runtime] -> %ss' % cls.lap

            case 'epoch':
                showtime = '[Epoch] -> %s' % ', '.join(
                    map(str, cls.travel[1:]))

            case Z:
                showtime = '[‼-ERROR-‼] -> %s' % (
                    'TIME STANDARD NOT FOUND: %s' % cls.std)

        return showtime

    @property
    def show(cls: Self,
             ) -> String:
        showtime = cls.string
        print(showtime)
        return showtime


Time = TIME(std='now')
Runtime = TIME(std='lap')
Crono = TIME(std='epoch')


class STUB(NotImplementedError):
    """
    Decorator @Stub | Object Stub.

    Decorates an incomplete function, indicating it has not been implemented yet.

    :Example:
        @Stub  # Prints the stub location when the function is called.
        Stub() # Prints the stub status, current line and module of call.
        Stub   # Null object with empty representation.

    :Instances:
        Stub = STUB()

    :Returns:
        R: Class | Callable
            | Decorated function or Stub object.
    """
    def __call__(cls: Self,
                 *args: Any,
                 **kwargs: Any,
                 ) -> Class or Callable:
        if len(args) == 1 and callable(args[0]):
            func = args[0]
            return cls._stubstatus(func)

        else:
            frame = cls._frame()
            print(
                f"[‼-STUB-‼]\n"
                f"In '{frame['file']}'\n"
                f"Ln {frame['line']}\n"
                f"Fn '{frame['function']}'"
            )
            return cls

    def _stubstatus(cls: Self,
                    func: Function,
                    ) -> Function:

        def Decorator(*args: Any,
                      **kwargs: Any,
                      ) -> Class:
            print(
                f"[‼-STUB-‼]\n"
                f"In '{inspect.getfile(func)}'\n"
                f"Ln {inspect.getsourcelines(func)[1]}\n"
                f"Fn '{func.__name__}'"
            )
            return Null

        return Decorator

    def _frame(cls: Self,
               ) -> inspect.Signature:
        frames = inspect.stack()

        for frame in frames[2:]:
            info = inspect.getframeinfo(frame[0])

            if "Stub" not in info.filename:
                return {
                    "file": info.filename,
                    "line": info.lineno,
                    "function": frame.function,
                }

        info = inspect.getframeinfo(frames[0][0])
        return {"file": info.filename, "line": info.lineno, "function": None}


Stub = STUB()


class NULL:
    """
    Null Object Pattern.

    A class that implements the Null Object Pattern by defining methods and operations that return neutral values or perform no actions.

    :Example:
        Null()           # Returns an instance of the NULL class.
        Null + 5         # Performs a no-op and returns Null itself.
        str(Null)        # Returns an empty string.
        Null.attribute   # Accesses a non-existent attribute, returns Null.
        Null == None     # Returns True, Null has equality to None.
        print(Null)      # Prints nothing, same as print().

    :Instances:
        Null = NULL()
    """
    Nal = lambda cls, *args, **kwargs: 0
    Nel = lambda cls, *args, **kwargs: ''
    Nil = lambda cls, *args, **kwargs: cls
    Nol = lambda cls, *args, **kwargs: None
    Nul = lambda cls, *args, **kwargs: False

    # Common methods
    __call__ = Nil
    __setattr__ = Nil
    __getattr__ = Nil
    __delattr__ = Nil
    __dir__ = lambda cls, *args, **kwargs: []

    # Comparison operations
    def __eq__(cls, other): return True if (
        (other is None) or (
            type(cls) == type(other))) else False
    __ne__ = Nul
    __lt__ = Nul
    __le__ = Nul
    __gt__ = Nul
    __ge__ = Nul

    # Arithmetic
    __add__ = __iadd__ = __radd__ = Nil
    __sub__ = __isub__ = __rsub__ = Nil
    __mul__ = __imul__ = __rmul__ = Nil
    __truediv__ = __itruediv__ = __rtruediv__ = Nil
    __floordiv__ = __ifloordiv__ = __rfloordiv__ = Nil
    __mod__ = __imod__ = __rmod__ = Nil
    __pow__ = __ipow__ = __rpow__ = Nil
    __matmul__ = __imatmul__ = __rmatmul__ = Nil

    # Binary
    __and__ = __iand__ = __rand__ = Nil
    __or__ = __ior__ = __ror__ = Nil
    __xor__ = __ixor__ = __rxor__ = Nil
    __lshift__ = __ilshift__ = __rlshift__ = Nil
    __rshift__ = __irshift__ = __rrshift__ = Nil

    # Unary
    __pos__ = Nil
    __neg__ = Nil
    __invert__ = Nil

    # Built-in math
    __abs__ = Nil
    __round__ = Nil
    __trunc__ = Nil
    __floor__ = Nil
    __ceil__ = Nil
    __divmod__ = Nil
    __rdivmod__ = Nil

    # Numeric conversions
    __int__ = Nal
    __float__ = lambda cls, *args, **kwargs: float('nan')
    __complex__ = lambda cls, *args, **kwargs: complex(float('nan'))

    # String | Text representation
    __repr__ = Nel
    __str__ = Nel
    __format__ = Nel
    # __bytes__ = lambda cls, *args, **kwargs: bytes(''.encode('utf-8'))
    __bool__ = Nul

    # Sequences
    __hash__ = Nul
    __len__ = Nal
    __index__ = Nil
    __contains__ = Nul
    __getitem__ = __setitem__ = Nil
    __iter__ = lambda cls, *args, **kwargs: iter([])
    __reversed__ = Nil
    __next__ = Nil
    __missing__ = Nil
    __length_hint__ = Nul

    # Context
    __enter__ = Nil
    __exit__ = Nil

    # Descriptors
    __set_name__ = Nil
    __get__ = Nil
    __set__ = Nil
    __delete__ = Nil

    # Class related methods
    __init_subclass__ = Nil
    def __mro_entries__(cls, bases): return tuple(bases)
    __class_getitem__ = Nil

    # Metaclass checks
    __instancecheck__ = Nul
    __subclasscheck__ = Nul

    # Async related methods
    __await__ = Nil
    __aenter__ = Nil
    __aexit__ = Nil
    __aiter__ = Nil
    __anext__ = Nil

    # Buffer related methods
    __buffer__ = lambda cls, *args, **kwargs: memoryview(
        bytes(''.encode('utf-8')))
    __release_buffer__ = Nil


Null = NULL()


class ERROR(NULL, Exception):
    """
    Error Object.

    A specialized version of the NULL class that represents an error state,
    overriding string and representation methods to return 'Error'.

    :Example:
        print(Error)
            - Error

        raise Error:
            - PlainTools.ERROR: Error

    :Instances:
        Error = ERROR()
    """
    __repr__ = lambda cls, *args, **kwargs: 'Error'
    __str__ = lambda cls, *args, **kwargs: 'Error'
    def __eq__(cls, other): return True if (
        type(cls) == type(other)) else False


Error = ERROR()


class MAIN:
    """
    Main script guard.

    Evaluates if the script is being executed directly;
    Similar to __name__ == '__main__'.

    :Example:
        if Main:     # Evaluates if __name__ == '__main__'.
        with Main:   # Enters the 'Main' context, only executes if Main.
        Main(*A,**K) # Invokes the 'Main' context; runs local 'main(*A,**K)'.

    :Methods:
        .time -> Float
            | Returns the script execution time.

        .showtime -> String
            | Displays the script execution time.

        .clear -> Self
            | Clears the console; Executed by .start.

        .start -> Self
            | Invokes .time & .clear.

        .end -> Self
            | Ends the program after debugging and logging.

    :Instances:
        Main = MAIN()

    :Returns:
        R: Bool = True if the script is being executed directly.
    """
    class MainguardError(BaseException):
        pass

    def __init__(cls: Self,
                 ) -> Class:
        cls.runtime = TIME(std='lap')
        cls.cycle = False
        cls.args = None
        cls.kwargs = None

    def __bool__(cls: Self,
                 ) -> Bool:
        return cls.mainguard

    def __call__(cls: Self,
                 *args: Any,
                 **kwargs: Any,
                 ) -> Bool:
        if cls.args is None:
            cls.args = args or None
        if cls.kwargs is None:
            cls.kwargs = kwargs or None
        ns = pframe(outer=True).f_locals
        if 'main' in ns and isinstance(ns['main'], Callable):
            if 'Main' in ns and ns['Main'] is cls:
                match cls.args, cls.kwargs:
                    case None, None:
                        exec("with Main: main()", ns)
                    case Z, None:
                        exec(f"with Main: main(*{cls.args})", ns)
                    case None, Z:
                        exec(f"with Main: main(**{cls.kwargs})", ns)
                    case X, Z:
                        exec(f"with Main: main(*{cls.args}, **{cls.kwargs})",
                             ns)

            else:
                pt = __import__(__name__)

                for k, v in ns.items():
                    if v == pt:
                        pt = k
                        break

                else:  # No break
                    return cls

                match cls.args, cls.kwargs:
                    case None, None:
                        exec(f"with {pt}.Main: main()", ns)
                    case Z, None:
                        exec(f"with {pt}.Main: main(*{cls.args})", ns)
                    case None, Z:
                        exec(f"with {pt}.Main: main(**{cls.kwargs})", ns)
                    case X, Z:
                        exec(
                            f"with {pt}.Main: main(*{cls.args},**{cls.kwargs})",
                            ns)

        return cls

    def __enter__(cls: Self,
                  ) -> Class:
        if cls.mainguard:
            cls.clear
            cls.start
            return cls

        else:
            sys.settrace(lambda *args, **keys: None)
            frame = inspect.currentframe().f_back
            frame.f_trace = cls.trace

    # stackoverflow.com/questions/60425503 <- Que hack absurdo!
    def trace(cls: Self,
              frame: Frame,
              event: String,
              arg: Any,
              ) -> BaseException:
        raise cls.MainguardError("Mainguard failed.")

    def __exit__(cls: Self,
                 exc_type: Type,
                 exc_val: BaseException,
                 exc_tb: Traceback,
                 ) -> Class:
        if isinstance(exc_val, cls.MainguardError):
            return True

        if exc_type is not None:
            exc_report = str(exc_type)
            start = exc_report.index("'") + 1
            end = exc_report.index("'", start)
            exc_report = exc_report[start:end]
            Logging('[‼-ERROR-‼] -> %s'.replace('E', 'MAIN:E') % exc_report)

        return cls.end

    @property
    def time(cls: Self,
             ) -> Float:
        return cls.runtime.time

    @property
    def showtime(cls: Self,
                 ) -> String:
        showtime = cls.runtime.string.replace('RUN', 'MAIN:')
        print(showtime)
        return showtime

    @property
    def clear(cls: Self,
              ) -> Class:
        clear()
        return cls

    @property
    def start(cls: Self,
              ) -> Class:
        if cls:
            # cls.clear
            cls.runtime()

        return cls

    @property
    def end(cls: Self,
            ) -> SystemExit:
        err = debug()
        skip()
        printc('[!-END-OF-FILE-!]', fill='=')
        skip()

        if err is not None:
            print('|= [‼-MAIN:ERROR-LOGGED-‼]')
            skip()

        if Logging.get:
            Logging.show.flush

        cls.showtime
        input()
        if not cls.cycle:
            exit()
        else:
            cls()

    @property
    def loop(cls: Self,
             ) -> Class:
        cls.cycle = True
        return cls

    @property
    def noloop(cls: Self,
               ) -> Class:
        cls.cycle = False
        return cls

    @property
    def mainguard(cls: Self,
                  ) -> Bool:
        return inspect.currentframe(
        ).f_back.f_back.f_globals['__name__'] == "__main__"


Main = MAIN()


class SILENCE:
    """
    Context manager that suppresses console output.

    Redirects stdout and stderr to /dev/null, effectively silencing
    all output within the context.

    :Example:
        with Silence:  # Silences all console output within the context.

    :Instances:
        Silence = SILENCE()

    :Returns:
        R: Class = Context manager that suppresses console output.
    """
    def __init__(cls: Self,
                 ) -> Class:
        cls.og_stdout = sys.stdout
        cls.og_stderr = sys.stderr
        cls.err = debug()

    def __str__(cls: Self,
                ) -> String:
        if cls.err is not None:
            return '\n'.join(cls.err)
        return ''

    def __repr__(cls: Self,
                 ) -> String:
        if cls.err is not None:
            return '\n'.join(cls.err)
        return ''

    def __enter__(cls: Self,
                  ) -> Class:
        cls.null_out = open(os.devnull, 'w')
        cls.err = debug()
        sys.stdout = cls.null_out
        sys.stderr = cls.null_out
        return cls

    def __exit__(cls: Self,
                 exc_type: Type,
                 exc_val: BaseException,
                 exc_tb: Traceback,
                 ) -> True:
        sys.stdout = cls.og_stdout
        sys.stderr = cls.og_stderr
        cls.err = debug()
        cls.null_out.close()
        return True


Silence = SILENCE()


class LOGGING:
    """
    Functional Logging.

    Stores provided strings or objects in an internal list;
    Writes them to a (filename).log file.

    :Example:
        Logging("message")  # Logs "message" in the internal list.
        Logging([1, 2, 3])  # Logs each element of the list on separate lines.

    :Args:
        obj: Any
            | Object(s) to be logged.

    :Methods:
        .get -> List
            | Returns the internal list of logged entries.

        .flush -> Self
            | Writes the current log to a file and clears the internal list.
            | This is automatically done at exiting the 'with Main' context.

        .show -> Self
            | Displays the stored messages from the log list.

        .reset -> list or None
            | Resets the internal list of logs to empty.

    :Instances:
        Logging = LOGGING()
    """
    def __init__(cls: Self,
                 *obj: Object,
                 ) -> Class:
        cls.obj = []
        cls._log = []
        cls.log_filename = None
        cls.last_filename = None
        cls.log_header = None

        if obj:
            cls(*obj)  # Redireciona para __call__

    def __call__(cls: Self,
                 *obj: Object,
                 ) -> Class:
        cls.obj = plist(obj)
        cls._log.extend(cls.obj)
        return cls

    def _file(cls: Self,
              ) -> None:
        caller = inspect.getmodulename(os.path.abspath(inspect.getfile(
            inspect.stack()[-1].frame)))
        cls.log_filename = caller + ".log"
        cls.log_header = [
            f"|‼ LOG•DATA\t{os.path.basename(cls.log_filename)}",
            f"|! System\t{platform.platform()}",
            f"|! Python\t{sys.version.strip().split(') [')[0]})",
            f"|! Platform\t[{sys.version.strip().split(') [')[1]}",
        ]

        if not os.path.exists(
                cls.log_filename) or not cls._valid(
                cls.log_filename):
            counter = 0
            new_log_filename = cls.log_filename

            while os.path.exists(new_log_filename) and not cls._valid(
                    new_log_filename):
                counter += 1
                new_log_filename = (
                    f"{os.path.splitext(cls.log_filename)[0]}_{counter}.log")

            cls.log_filename = new_log_filename
            cls._create(cls.log_filename)

    def _valid(cls: Self,
               filename: String,
               ) -> Bool:
        if not os.path.exists(filename):
            return False

        expected_header = [line + "\n" for line in cls.log_header]

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

            if len(lines) < 4:
                return False

            for i in range(4):

                if lines[i].strip() != expected_header[i].strip():
                    return False

            return True

    def _create(cls: Self,
                filename: String,
                ) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(cls.log_header) + "\n\n")

    def _write(cls: Self,
               message: Object,
               ) -> None:
        if cls.log_filename is None:
            cls._file()

        with open(cls.log_filename, "a", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S:%f")[:-3]
            file.write(f"|= {timestamp}\n")

            for msg in plist(message):
                file.write(f"|> {msg}\n")
            file.write("\n")

    @property
    def get(cls: Self,
            ) -> List[String]:
        return cls._log

    @property
    def name(cls: Self,
             ) -> String:
        caller = inspect.getmodulename(os.path.abspath(inspect.getfile(
            inspect.stack()[-1].frame)))
        cls.last_filename = caller + ".log"
        cls.log_header = [
            f"|‼ LOG•DATA\t{os.path.basename(cls.last_filename)}",
            f"|! System\t{platform.platform()}",
            f"|! Python\t{sys.version.strip().split(') [')[0]})",
            f"|! Platform\t[{sys.version.strip().split(') [')[1]}",
        ]

        if not os.path.exists(
                cls.last_filename) or not cls._valid(
                cls.last_filename):
            counter = 0
            new_log_filename = cls.last_filename

            while os.path.exists(new_log_filename) and not cls._valid(
                    new_log_filename):
                counter += 1
                new_log_filename = (
                    f"{os.path.splitext(cls.last_filename)[0]}_{counter}.log")

            cls.last_filename = new_log_filename

        return cls.last_filename

    @property
    def flush(cls: Self,
              ) -> Class:
        if cls._log:
            cls._write(cls._log)
            cls._log = []

        return cls

    @property
    def show(cls: Self,
             ) -> Class:
        if not cls._log:
            return cls

        print(f"|‼ LOG•DATA @{cls.name}")
        print(f"\n|= {datetime.datetime.now().strftime('%d/%m/%YYYY')[:-3]}")

        for i in cls._log:
            print('|> ' + str(i))

        skip()
        return cls

    @property
    def reset(cls: Self,
              ) -> List[String] or None:
        cls._log = []
        return cls._log


Logging = LOGGING()


class TRY:
    """
    Try Context.

    A simpler 'try' context, with no direct error handling;
    Can be done in a verbose way by the use of 'with Try.show:' method.

    :Example:
        with Try:  # Begins execution and tracks its success or failure.

    :Methods:
        .show -> Self
            | Enables verbose mode to print the context's progress and results.

    :Properties:
        verbose: Bool = False
            | Controls whether to print the result to the console.

        result: String
            | Stores the result of the try block, indicating success or failure.
    """
    def __init__(cls: Self,
                 ) -> None:
        cls.verbose = False
        cls.result = ''

    def __enter__(cls: Self,
                  ) -> None:
        frame = inspect.currentframe()

        while True:
            backframe = frame.f_back

            if backframe is None:
                break

            frame = backframe

        cls.entry = frame.f_lineno
        cls.result = f'[!-TRYING-!] -> Ln {cls.entry}'

        if cls.verbose:
            print(cls.result)

        cls.warnings_manager = warnings.catch_warnings()
        cls.warnings_manager.__enter__()
        warnings.simplefilter("error")
        return cls

    def __str__(cls: Self,
                ) -> String:
        return cls.result

    def __repr__(cls: Self,
                 ) -> String:
        return cls.result

    def __exit__(cls: Self,
                 *args: Any,
                 ) -> True:

        if args[0] is not None:
            cls.err = debug()
            cls.exitcode = str(cls.err[-1])
            cls.exitline = str(cls.err[-2])
            cls.result = f'[!-FAIL-!] -> {cls.exitline} -> {cls.exitcode}'

        else:
            cls.exitline = str(inspect.stack()[-1])
            cls.exitline_start = cls.exitline.index('end_lineno=') + 11
            cls.exitline_end = cls.exitline.index(',', cls.exitline_start)
            cls.exit = int(
                cls.exitline[cls.exitline_start:cls.exitline_end])
            cls.result = f'[!-SUCCESS-!] -> Ln {cls.exit}'

        if cls.verbose:
            print(cls.result)

        return True

    @property
    def show(cls: Self,
             ) -> Class:
        cls.verbose = True
        return cls


Try = TRY()


class LINES:
    """
    Line Number Context Manager.

    A context manager that prefixes each line of output with the line number.

    :Example:
        with Lines:
            print("Hello, World!")  # Output will be prefixed with line no.

    :Instances:
        Lines = LINES()
    """
    def __enter__(cls):
        cls.stdout = sys.stdout
        sys.stdout = cls

    def __exit__(cls, exc_type, exc_value, traceback):
        sys.stdout = cls.stdout

    def write(cls, msg):
        if msg != '\n':
            frame = inspect.currentframe()

            while True:
                backframe = frame.f_back
                if backframe is None:
                    break
                frame = backframe

            line_no = frame.f_lineno
            cls.stdout.write(f"|Ln {line_no}| {msg}")

        else:
            cls.stdout.write(msg)


Lines = LINES()


class SEVAL:
    """
    Safe Expression Evaluator.

    A secure alternative to Python's `eval()` function, designed to evaluate
    mathematical and basic expressions while preventing access to unsafe
    operations and functions.

    Its default protocol is 'blacklist', but a new instance of 'SEVAL()' can
    be initiated in the 'whitelist' mode to further restrict access to unsafe
    operations and functions. This can be done as:

        SevalW = SEVAL('whitelist')

        SevalW.whitelist.modules |= {'math'} # Allows using 'math' module.

        SevalW.whitelist.functions |= {'round'} # Allows using 'round()'.

    Beware that instantiating 'SEVAL()' in this mode prohibits  the
    evaluation of any variables in the current namespace unless their
    names are explicitly whitelisted beforehand.

    Because of how Python works, objects defined and imported inside the
    PlainTools package itself are accessible to the class. Unsafe operators
    and packages, such as 'os' and 'sys', are still blacklisted though.

    To check the complete default 'blacklist'

    :Example:
        Seval("2 + 2")  # Returns 4

        Seval("round(math.pi * 2, 2)")  # Returns 6.28 if 'math' is imported.

        Seval("import shutil; shutil.rmtree('/.')")  # Raises UnsafeError.

    :Raises:
        UnsafeError: Raised when tries unsafe operation, function, or module.

    :Attributes:
        UnsafeError: TypeError
            | Custom error for handling unsafe operations.

        blacklist: dict
            | Defines disallowed functions and modules that are prohibited.
    """
    class UnsafeError(TypeError):
        pass

    def __init__(cls,
                 protocol: String = 'blacklist',
                 functions: Set = set(),
                 modules: Set = set(),
                 ) -> Class:
        cls.namespace = collections.ChainMap(pframe(2).f_locals,
                                             pframe(outer=True).f_locals,
                                             moduleview('builtins'),
                                             )
        cls.operators = {ast.Add: operator.add,
                         ast.Sub: operator.sub,
                         ast.Mult: operator.mul,
                         ast.Div: operator.truediv,
                         ast.FloorDiv: operator.floordiv,
                         ast.Mod: operator.mod,
                         ast.Pow: operator.pow,
                         ast.UAdd: operator.pos,
                         ast.USub: operator.neg,
                         ast.LShift: operator.lshift,
                         ast.RShift: operator.rshift,
                         ast.BitOr: operator.or_,
                         ast.BitXor: operator.xor,
                         ast.BitAnd: operator.and_,
                         }
        # 'blacklist' | 'whitelist'
        cls.protocol = protocol if protocol == 'whitelist' else 'blacklist'
        cls.permitlist = dict(functions=functions, modules=modules)
        cls.blacklist = Container(cls.permitlist if all(
            cls.permitlist.values()) else ()) or (
                Container(functions={'eval',
                                     'exec',
                                     'exit',
                                     'compile',
                                     '__import__',
                                     '__file__',
                                     '__path__',
                                     '__main__',
                                     'dir',
                                     'moduleview',
                                     'pimport',
                                     'pframe',
                                     'print',
                                     'printnl',
                                     'printc',
                                     'doc',
                                     'site',
                                     'qfunc',
                                     'timeout',
                                     'let',
                                     'const',
                                     'Constant',
                                     'skip',
                                     'clear',
                                     'debug',
                                     'eof',
                                     'deepframe',
                                     'evinput',
                                     'input',
                                     'showcall',
                                     'raise',
                                     'open',
                                     'LOGGING',
                                     'Logging',
                                     'Constant',
                                     'getattr',
                                     'setattr',
                                     'delattr',
                                     'hasattr',
                                     'base64',
                                     'bytes',
                                     'bytearray',
                                     'decode',
                                     'encode',
                                     'open',
                                     'main',
                                     'Main',
                                     'MAIN',
                                     'seval',
                                     'Seval',
                                     'SEVAL',
                                     'blacklist',
                                     'whitelist',
                                     'protocol',
                                     },
                          modules={'os',
                                   'sys',
                                   'shutil',
                                   'pathlib',
                                   'glob',
                                   'pathlib',
                                   'tempfile',
                                   'stat',
                                   'socket',
                                   'http',
                                   'ftplib',
                                   'smtlib',
                                   'urllib',
                                   'platform',
                                   'getpass',
                                   'pwd',
                                   'grp',
                                   'uuid',
                                   'ctypes',
                                   'resource',
                                   'ssl',
                                   'hashlib',
                                   'secrets',
                                   'crypt',
                                   'code',
                                   'codeop',
                                   'compileall',
                                   'xmlrpc',
                                   'json',
                                   'sqlite3',
                                   'dbm',
                                   'mmap',
                                   'gc',
                                   'webbrowser',
                                   'tk',
                                   'turtle',
                                   'pdb',
                                   'sysconfig',
                                   'atexit',
                                   'faulthandler',
                                   'unittest',
                                   'builtins',
                                   'threading',
                                   'asyncio',
                                   'subprocess',
                                   'multiprocessing',
                                   'signal',
                                   'base64',
                                   're',
                                   },
                          )
        )
        cls.whitelist = Container(cls.permitlist)

    def __call__(cls, expression):
        if not isinstance(expression, str):
            expression = repr(expression)
        try:
            tree = ast.parse(expression, mode='eval')
        except SyntaxError:
            raise cls.UnsafeError("Invalid syntax in expression")

        try:
            node = tree.body
            return cls.ndeval(node, cls.namespace)
        except BaseException as e:
            raise e

    def ndeval(cls, node, local):
        if isinstance(node, ast.Constant):  # Numbers and Constants
            return node.value

        elif isinstance(node, ast.BinOp):  # Binary ops
            if type(node.op) in cls.operators:
                return cls.operators[type(node.op)](cls.ndeval(
                    node.left, local), cls.ndeval(node.right, local))
            else:
                raise cls.UnsafeError("Operation not allowed")

        elif isinstance(node, ast.UnaryOp):  # Unary ops
            if type(node.op) in cls.operators:
                return cls.operators[type(node.op)](
                    cls.ndeval(node.operand, local))
            else:
                raise cls.UnsafeError("Operation not allowed")

        elif isinstance(node, ast.Name):  # Variables
            if node.id in local:
                func = local[node.id]
                if callable(
                        func) and ((cls.protocol == 'blacklist' and (
                            func.__name__ in cls.blacklist['functions']) or (
                                cls.protocol == 'whitelist' and (
                                    func.__name__ not in cls.whitelist[
                                        'functions'])))):
                    raise cls.UnsafeError(
                        f"Function '{node.id}' is not allowed")
                return func
            elif node.id in {
                'getattr', '__class__', '__bases__', '__globals__',
                    '__code__', '__closure__'}:
                raise cls.UnsafeError(f"Access to '{node.id}' is not allowed")
            else:
                raise NameError(f"Name '{node.id}' is not defined")

        elif isinstance(node, ast.Attribute):  # Attrs
            value = cls.ndeval(node.value, local)
            if isinstance(
                    node.value,
                    ast.Name) and ((cls.protocol == 'blacklist' and (
                        node.value.id in cls.blacklist['modules'])) or (
                            cls.protocol == 'whitelist' and (
                                node.value.id not in cls.whitelist['modules']
                            ))):
                raise cls.UnsafeError(
                    f"Access to module '{node.value.id}' is not allowed")
            if node.attr in {
                '__class__',
                '__bases__',
                '__globals__',
                '__code__',
                    '__closure__'}:
                raise cls.UnsafeError(
                    f"Access to attribute '{node.attr}' is not allowed")
            return getattr(value, node.attr)

        elif isinstance(node, ast.Call):  # Calls
            if isinstance(
                    node.func,
                    ast.Name) and (cls.protocol == 'blacklist' and (
                        node.func.id in cls.blacklist['functions']) or (
                            cls.protocol == 'whitelist' and (
                                node.func.id not in cls.whitelist['functions']
                            ))):
                raise cls.UnsafeError(
                    f"Function '{node.func.id}' is not allowed")
            func_name = cls.ndeval(node.func, local)
            if ((cls.protocol == 'blacklist' and (
                func_name.__name__ in cls.blacklist['functions'])) or (
                    cls.protocol == 'whitelist' and (
                        func_name.__name__ not in cls.whitelist['functions']
                    ))):
                raise cls.UnsafeError(
                    f"Function '{func_name.__name__}' is not allowed")
            if not callable(func_name):
                raise cls.UnsafeError("Calling non-callable")

            args = [cls.ndeval(arg, local) for arg in node.args]
            return func_name(*args)

        else:  # None case
            raise cls.UnsafeError("Expression not allowed")


Seval = SEVAL()


# CONSTRUCTOR CLASSES ==> Custom objects:
class Container(Dict):
    """
    Container Class; dict Subclass.

    A flexible dict-class that supports various operations and
    transformations. Unlike a standard dictionary, a `Container`
    is unpacked by its items rather than by its keys.

    Note: Containers can't have numeric keys due to how their
    keys are directly associated to its instance attributes.
    However, any String type is a valid key type.
    Attempting to update a Container instance with
    enumerated dictionaries will raise a TypeError.


    The Container supports basic arithmetic operations on a
    per-key basis, meaning that you can operate an iterable
    to a Container, where each ordered element operates each
    key's value until exhaustion; Where as single, non-iterable
    operations are performed on the entire Container.

    Containers can have its values accessed as attributes
    when calling for their keys. This means that assigned
    attributes into this class are also added to the
    Container's keys with the designated value.

    :Example:
        C1 = Container(a=1, b=2)
            | Creates a Container as {'a': 1, 'b': 2}

        C2 = Container('c')
            | Creates a Container as {'c': None}

        C1(C2) # Same as C1 += C2
            | Aggregates C1 and C2 for {'a': 1, 'b': 2, 'c': None}

        C1.fill(4)
            | Alocates '4' to the first encounter of `None` value in C1.

    :Methods:
        .sort(*args, **kwargs): Self
            | Sorts the keys (or values) of the Container; Optional lambda.

        .shove(*vals): Self
            | Adds the values to the keys following the current order of keys.

        .fill(*vals, target=None, exhaust=True): Self
            | Fills in any `target` vals in the Container with given vals.
            | `target` argument can be a lambda|function|builtin|singleton.
            | `exhaust` argument defines if fill is finite or cyclic infinite.

        .order(*keys): Self
            | Orders the keys of the Container as provided.

        .only(*keys): Self
            | Returns a Container containing only the specified keys.

        .without(*keys): Self
            | Returns a Container without the specified keys.

        .keyval(): dict
            | Returns a copy of the dictionary object as {keys: values}.

        .key(*keys): list
            | Returns a list of keys in Container; Optional filter for values.

        .val(*vals): list
            | Returns a list of values in Container; Optional filter for keys.

        .sub(): Tuple[Container]
            | Returns a tuple of each k: v pair in Container, as Containers.

        .copy(): Container
            | Returns a deepcopy of the current Container.

    :Operators:
        Any basic arithmetic operator is supported as in:
        Container <> Container;
        Container <> other (if the operation(value, other) is valid).

        Operations with non-iterables are valid as long as the operation to
        every Container[N] <> other is valid for all given N.
            | i.e. Container(f=1, g=2, h=3) * 2 == Container(f=2, g=4, h=6)
            | i.e. Container(Bob='Foo') - 5 == Container(Bob='Foo', Bob_1=5)

        Operations with iterables are valid as long as the operation to
        every pair Container[N] <> other[N] is valid for the max possible N.
            | i.e. Container(R=5, S=10) * (2,3,4) == Container(R=10, S=30)
            | i.e. Container(T=2,U=4,V=6) - {2,3} == Container(T=0, U=1, V=6)

        Remainder of Container <> Other operations are ignored, as the result
        is a Container type with the same keys as the involved Container.
            | i.e. Container(i=2, j=3) * [2, 3, 4] == Container(i=4, j=9)

        Remainer of Container <> Container operations aggregate non-similar
        keys into the final result, unmodified, as no C1[K] <> C2[K] is valid.
            | i.e. Container(f=5) - Container(g=10) == Container(f=5, g=10)

        add (+)
            | Adds the values of another Container, or from a sequence.
            | i.e. Container(a=5) + (b=4) == Container(a=5, b=4)
            | i.e. Container(a=5, b=4) + [3, 4] == Container(a=8, b=8)

        sub (-)
            | Subtracts the values of another Container or from a sequence.
            | i.e. Container(x=5, y=10) - 3 == Container(x=2, y=7)
            | i.e. Container(a=5, b=4) - Container(c=3, d=2)

        mul (*)
            | Multiplies the values of another Container or from a sequence.
            | i.e. Container(x=5) * 2 == Container(x=10)
            | i.e. Container(x=5, y=4) * (3, 4) == Container(x=15, y=16)

        truediv (/)
            | Divides the values of another Container or from a sequence.
            | i.e.Container(T=2,U=4,V=6)/[1,2,3]==Container(T=2.0,U=2.0,V=2.0)

        floordiv (//)
            | Floor divides the values of another Cont. or from a sequence.
            | i.e. Container(A=12.5) // Container(A=3.5) == Container(A=3.0)

        mod (%)
            | Modulo operates on the values of another Cont. or from a seq.
            | i.e. Container(B=7.5) % Container(B=2) == Container(B=1.5)

        pow (**)
            | Raises the values of the Container to the power of.
            | i.e. Container(C=5) ** Container(C=3) == Container(C=125)
    """
    def __init__(cls, *args, **kwargs):
        cls(*args, **kwargs)  # Redirect to __call__

    def __call__(cls, *args, **kwargs):
        for arg in args:

            if isinstance(arg, dict):
                cls.update(arg)
                continue

            elif isinstance(arg, (list, tuple, set)):
                cls.update(zip(
                    cls.keys(), arg))

            else:
                cls.update(zip(
                    args, kwargs.get('value', [None] * len(args))))

        for kwarg in kwargs:
            cls[kwarg] = kwargs[kwarg]

        for key in cls.key():
            if not hasattr(Container, key):
                super().__setattr__(key, cls[key])

        return cls

    def __getitem__(cls, key):
        if isinstance(key, int):

            with Try:
                item = tuple(cls.items())[key]
                return item

        else:
            return super().__getitem__(key)

    def __getattr__(cls, key):
        with Try:
            return cls[key]
        with Try:
            return super().__getattr__(key)

    def __setattr__(cls, key, val):
        if not hasattr(Container, key) or key in cls:
            cls[key] = val

        return cls

    def __iter__(cls):
        return iter(cls.items())

    def sort(cls, *args, **kwargs):
        items = list(cls.items())

        items.sort(*args, **kwargs)

        cls.clear()

        for key, val in items:
            cls[key] = val

        return cls

    # METHODS ─► Value Allocation:
    def shove(cls, *vals):
        for key, val in zip(cls.keys(), vals):
            cls[key] = val

        return cls

    def fill(cls, *vals, target=None, exhaust=True):
        vals = list(vals)

        for key in cls.keys():

            if any(pistype(target, Function, Builtin)):
                if target((cls[key],)) or target(cls[key]):
                    try:
                        cls[key] = vals[0]
                        if not exhaust:
                            vals.append(vals[0])
                        vals.pop(0)
                    except IndexError:
                        break

            else:
                if cls[key] == target:
                    try:
                        cls[key] = vals[0]
                        if not exhaust:
                            vals.append(vals[0])
                        vals.pop(0)
                    except IndexError:
                        break

        return cls

    # METHODS ─► Key Allocations:
    def order(cls, *keys):
        items = list(cls.items())

        cls.clear()

        for key in keys:

            for ikey, ival in items:

                if ikey == key:
                    cls[key] = ival
                    break

        for ikey, ival in items:

            if ikey not in keys:
                cls[ikey] = ival

        return cls

    def only(cls, *keys):
        keys = list(keys)

        for key in cls.key:
            if key not in keys:
                cls.pop(key)

        return cls

    def without(cls, *keys):
        keys = list(keys)

        for key in cls.key:
            if key in keys:
                cls.pop(key)

        return cls

    # METHODS ─► Container Access:
    def keyval(cls):
        return dict(zip(cls.keys(), cls.values()))

    def key(cls, *keys):
        return list(cls.keys()) if not keys else punit([
            cls[key] for key in keys])

    def val(cls, *vals):
        return list(cls.values()) if not vals else punit([
            key for key in cls.keys() if cls[key] in vals])

    def sub(cls):
        return tuple(Container(key).shove(val) for key, val in cls)

    def copy(cls):
        return Container(cls.keyval())

    def operate(cls, other, op):
        result = Container(cls.copy())
        if isinstance(other, dict):
            for key in other.keys():
                if key in cls:
                    try:
                        if result[key] is not None:
                            result[key] = op(cls[key], other[key])
                        else:
                            result[key] = other[key]
                    except Exception:
                        suffix_index = 1
                        new_key = f"{key}_{suffix_index}"

                        while new_key in result:
                            suffix_index += 1
                            new_key = f"{key}_{suffix_index}"

                        result[new_key] = other[key]

                else:
                    result[key] = other[key]

        elif isinstance(other, Iterable) and not isinstance(other, str):
            other = plist(other)
            for i, key in enumerate(cls.keyval()):
                if i < len(other):
                    try:
                        result[key] = op(cls[key], other[i])
                    except Exception:
                        idx = 1
                        ikey = f"{key}_{idx}"

                        while ikey in result:
                            idx += 1
                            ikey = f"{key}_{idx}"

                        result[ikey] = other[i]

        else:
            for key in cls.keyval():
                try:
                    result[key] = op(cls[key], other)

                except TypeError:
                    continue  # ie. NoneTypes

                except Exception:
                    idx = 1
                    ikey = f"{key}_{idx}"

                    while ikey in result:
                        idx += 1
                        ikey = f"{key}_{idx}"

                    result[ikey] = other

        return result

    def convert(cls, x, y, op):
        try:
            return op(x, y)
        except TypeError:
            try:
                return op(x, type(x)(y))
            except (TypeError, ValueError):
                try:
                    return op(type(y)(x), y)
                except (TypeError, ValueError):
                    raise

    def __add__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a + b))

    def __sub__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a - b))

    def __mul__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a * b))

    def __truediv__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a / b))

    def __floordiv__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a // b))

    def __mod__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a % b))

    def __pow__(cls, other):
        return cls.operate(other, lambda x, y: cls.convert(
            x, y, lambda a, b: a ** b))


class Constant:
    """
    Immutable Constants.

    Wraps a value and provides a constant, immutable interface to it.

    Overrides most of the standard dunder methods to ensure immutability.

    Non-dunder methods can be called, but will only return the Constant's
    value and won't modify the Constant itself or it's value in any way.

    :Proto-Code:
        If a (Variable) is a (Value) wrapped as a (Constant):
          | The (Variable)'s (Value) becomes an immutable (Constant).

        The (Variable)'s (Name) can still be reassigned or deleted,
        but the (Variable)'s (Value) cannot be changed.

        Return the original (Value) of the (Constant).

    :Examples:
        x = Constant(5)
            | Create an immutable constant with a value of 5
            | i.e. x + 5 == 10
            | i.e. x += 5 ; x == 5

        pi = Constant(math.pi)
            | Assign 'math.pi' to 'pi' as an immutable constant
            | i.e. const(rpi=pi*2)

    :Args:
        value: Any
          | The value to be wrapped as a Constant.

    :Returns:
        Constant
          | An immutable Constant instance wrapping the provided value.
    """

    # Core methods
    def __init__(cls, value): return object.__setattr__(cls, 'val', value)

    def __getattr__(cls, name):
        attr = getattr(cls.val, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                return cls
            return wrapper
        return attr

    def inplace(cls, *args, **kwargs):
        return Constant(cls.val)

    def other(signal):
        def wrapper(cls, other):
            try:
                return eval(f"cls.val {signal} other")
            except Exception:
                return eval("cls.val")
        return wrapper

    # In-place operators
    __setattr__ = inplace
    __delattr__ = inplace
    __iadd__ = inplace
    __isub__ = inplace
    __imul__ = inplace
    __itruediv__ = inplace
    __ifloordiv__ = inplace
    __imod__ = inplace
    __ipow__ = inplace
    __imatmul__ = inplace
    __iand__ = inplace
    __ior__ = inplace
    __ixor__ = inplace
    __ilshift__ = inplace
    __irshift__ = inplace

    # Comparison operations
    __eq__ = other('==')
    __ne__ = other('!=')
    __lt__ = other('<')
    __le__ = other('<=')
    __gt__ = other('>')
    __ge__ = other('>=')

    # Arithmetic
    __add__ = __radd__ = other('+')
    __sub__ = __rsub__ = other('-')
    __mul__ = __rmul__ = other('*')
    __truediv__ = __rtruediv__ = other('/')
    __floordiv__ = __rfloordiv__ = other('//')
    __mod__ = __rmod__ = other('%')
    __pow__ = __rpow__ = other('**')
    __matmul__ = __rmatmul__ = other('@')

    # Binary
    __and__ = __rand__ = other('&')
    __or__ = __ror__ = other('|')
    __xor__ = __rxor__ = other('^')
    __lshift__ = __rlshift__ = other('<<')
    __rshift__ = __rrshift__ = other('>>')

    # Unary
    def __pos__(cls): return Constant(+cls.val)
    def __neg__(cls): return Constant(-cls.val)
    def __invert__(cls): return Constant(~cls.val)

    # Built-in math
    def __abs__(cls): return abs(cls.val)
    def __index__(cls): return int(cls.val) if isinstance(
        cls.val, Number) else NotImplemented

    def __round__(cls, ndigits=0): return round(cls.val, ndigits)

    def __trunc__(cls): return int(cls.val) if isinstance(
        cls.val, float) else NotImplemented

    def __floor__(cls): return int(cls.val // 1) if isinstance(
        cls.val, float) else NotImplemented
    def __ceil__(cls): return int(cls.val // 1 + 1) if isinstance(
        cls.val, float) and cls.val % 1 != 0 else int(cls.val)

    def __divmod__(cls, other): return divmod(cls.val, other)
    def __rdivmod__(cls, other): return divmod(other, cls.val)

    # Numberic conversions
    __complex__ = __int__ = __float__ = __index__ = (
        lambda cls: type(cls.val)(cls.val))

    # String | Text representation
    def __repr__(cls): return repr(cls.val)
    def __str__(cls): return str(cls.val)
    def __format__(cls, format_spec): return format(cls.val, format_spec)
    def __bytes__(cls): return bytes(cls.val)
    def __bool__(cls): return bool(cls.val)

    # Sequences
    def __hash__(cls): return hash(cls.val)
    def __len__(cls): return len(cls.val)
    def __contains__(cls, item): return item in cls.val
    __getitem__ = __setitem__ = lambda cls, key: cls.val[key]
    def __iter__(cls): return iter(cls.val)
    def __reversed__(cls): return reversed(cls.val)
    def __next__(cls): return next(cls.val)
    def __missing__(cls): return Constant(cls.val)
    def __length_hint__(cls): return len(cls.val)

    # Context
    def __enter__(cls): return cls.val.__enter__()
    __exit__ = lambda cls, *args: cls.val.__exit__(*args)

    # Descriptors
    def __dir__(cls): return dir(cls.val)
    def __set_name__(cls, owner, name): return None
    def __get__(cls, instance, owner=None): return cls.val
    def __set__(cls, instance, value): return None
    def __delete__(cls, instance): return None

    # Class related methods
    def __init_subclass__(cls): return None
    def __mro_entries__(cls, bases): return tuple(bases)
    def __class_getitem__(cls, item): return cls

    # Metaclass checks
    def __instancecheck__(cls, instance): return isinstance(instance, cls)
    def __subclasscheck__(cls, subclass): return issubclass(subclass, cls)

    # Async related methods
    def __await__(cls): return cls.val.__await__()
    def __aenter__(cls): return cls.val.__aenter__()
    __aexit__ = lambda cls, *args: cls.val.__aexit__(*args)
    def __aiter__(cls): return cls.val.__aiter__()
    def __anext__(cls): return cls.val.__anext__()

    # Buffer related methods
    def __buffer__(cls, flags): return memoryview(cls.val)
    def __release_buffer__(cls, view): return None


# DOCUMENTATION ==> Module documentation access:
def doc(*objs: callable,
        verbose: bool = True,
        ) -> List[String] | Null:
    """
    Docstring Printer.

    :Rationale:
        Prints into the console any docstring associated with the given
        object(s) or its parent class(es), headed by its origin module.

        Prints the current frame's module docstring if no object is given.
    """
    R: List[String] = []
    L: List[String] = ('__kmodule__', '__class__', '__name__', '__doc__')
    objs = list(objs)

    if objs:
        if verbose:
            printc("#", fill="#")

        for obj in objs:
            try:
                if obj.__doc__ is not None:
                    if verbose:
                        for attr in L:
                            if hasattr(obj, attr):
                                print(getattr(obj, attr))
                        printc("#", fill="#")
                    R.append(obj.__doc__)

            except AttributeError:
                objs.append(obj.__class__)
                continue

    else:
        if verbose:
            print(pframe(2).f_globals['__doc__'] or Null)

    return R if R else Null


def site(module: Module | str = '__main__',
         ) -> None:
    """
    Documentation HTML Viewer.

    This function will search for any .html files in the module's
    directory that are named after the module itself, and attempt
    to open it in the default browser of the user.
    """
    import webbrowser
    if isinstance(module, str):
        module = pimport(module)
        
    if hasattr(module, '__url__'):
        # https://stackoverflow.com/a/29854274/26469850
        import http.client
        conn = http.client.HTTPSConnection("8.8.8.8", timeout=1)
        err = False
        try:
            conn.request("HEAD", "/")
            webbrowser.open(module.__url__)
        except BaseException:
            err = True
        finally:
            conn.close()
            if not err:
                return
    
    name = os.path.basename(module.__file__).split('.')[0] if hasattr(
        module, '__file__') else module.__name__
    
    sites = glob.glob('**/*.html', recursive=True)

    for site in sites:
        if f"{name}Docs" in site:
            webbrowser.open(os.path.abspath(site))
            break
    else:
        print(f'Site for {name} documentation not found.\n' + (
            f'Note: [{name}] documentation must be a .html file ') + (
                f"containing '{name}Docs' in its name, ") + (
                    f"or an URL defined in {name}.__url__ attribute.\n")
        )


with Main:
    doc()
    site()
