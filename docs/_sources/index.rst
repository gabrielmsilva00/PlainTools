.. PlainTools documentation master file, created by
   sphinx-quickstart on Fri Jul 12 13:32:04 2024.

**PlainTools' Docs**
---------------------

**Welcome to PlainTools' documentation!**

PlainTools is a Python 3 library designed to streamline simple operations, 
loops and contexts with easy to handle classes and functions.

- `Library's Github <https://github.com/gabrielmsilva00/PlainTools>`_
- `Author's Github <https://github.com/gabrielmsilva00>`_

(Click below onto each [Section] to expand | collapse it.)

.. collapse:: [Table of Contents]

    - :ref:`Formatter Functions`
        Formatted data in an easy way.
            - :py:func:`pt.plist`
            - :py:func:`pt.punit`
            - :py:func:`pt.pnumber`
            - :py:func:`pt.pdecimals`
            - :py:func:`pt.pstring`
            - :py:func:`pt.pistype`
            - :py:func:`pt.prange`
            - :py:func:`pt.pinterval`
            - :py:func:`pt.psequence`
            - :py:func:`pt.pindex`
            - :py:func:`pt.pminmax`
            - :py:func:`pt.plen`
            - :py:func:`pt.pabs`
            - :py:func:`pt.psum`
            - :py:func:`pt.pimport`
            - :py:func:`pt.pframe`


    - :ref:`Statement & Extension Functions`
        Powerful, close to native syntax and easy to use.
            - :py:func:`pt.let`
            - :py:func:`pt.const`
            - :py:func:`pt.printnl`
            - :py:func:`pt.printc`
            - :py:func:`pt.doc`
            - :py:func:`pt.skip`
            - :py:func:`pt.evinput`
            - :py:func:`pt.timeout`
            - :py:func:`pt.loop`
            - :py:func:`pt.showcall`


    - :ref:`Debugger & Utility Functions`
        Easy debugging management with console operations.
            - :py:func:`pt.debug`
            - :py:func:`pt.clear`
            - :py:func:`pt.eof`
            - :py:func:`pt.deepframe`

    - :ref:`Operator & Instantiated Classes`
        Ready-to-use instances of functional objects.
            - :py:class:`pt.TIME`
            - :py:class:`pt.STUB`
            - :py:class:`pt.NULL`
            - :py:class:`pt.ERROR`
            - :py:class:`pt.MAIN`
            - :py:class:`pt.SILENCE`
            - :py:class:`pt.LOGGING`
            - :py:class:`pt.TRY`
            - :py:class:`pt.LINES`
            - :py:class:`pt.SEVAL`

    - :ref:`Constructor Classes & Custom Objects`
        Custom object constructors.
            - :py:class:`pt.Container`
            - :py:class:`pt.Constant`

ㅤ

.. collapse:: [Introduction]

    The following needs to be considered when reading these docs:

    - It is encouraged that you use the suggested convention:
        - import PlainTools as pt

    - It is assumed that you know the basics of Python's data types. 
        Type annotations were made in a more verbose way, with:
            - X: Integer

        Instead of:
            - X: int

        Unfamiliar types like 'Real' can be associated with what
        meaning they first convey: 
        
        Having a variable declared as:
            - Y: Real
        
        Is the same as:
            - Y: int | float | decimal.Decimal | fractions.Fraction
        
        And is itself similar or very closely related to 'numbers.Real'.

    Any documentation found here can be similarly provided in the Python 
    context or environment running this module by the use of the 
    :py:func:`pt.doc` function as:

        - pt.doc(\*objs)
            - Where `objs` is the desired function(s) or class(es) to obtain documentation from.

    This will print the target's documentation, if any, to the current `console` 
    or `stdout` in general.

ㅤ

.. collapse:: [Resources & Credits]

    - Disclaimer\: :orange:`LLM (AI)` Use\:
        - `ChatGPT <https://chat.openai.com>`_, `Codeium <https://codeium.com>`_ and `Gemini <https://gemini.google.com>`_ (The later not credited as it did not "contribute" directly to the codebase) were used in this project development.
        - If you, your university or your company (in general, if the target for this library's use) does have any restrictions, implicit or explicit, against the use of LLMs in production | academic coding, please avert from using this library.
        - Any code "contributed" by or taken from any LLM (AI) use, prompted directly or indirectly, was heavily debugged and tested (to the best of my personal capacity).
        - If any code comes across as sluggish, unnoptimized or just bad, please let me know by raising an issue or DMing me at GitHub (`@gabrielmsilva00 <https://github.com/gabrielmsilva00>`_), or email me at `@gabrielmaia.silva00@gmail.com <mailto:gabrielmaia.silva00@gmail.com?subject=PlainTools%20Python%20Library%20Feedback>`_.
        - For a more clear understanding of the above, you will probably find 40~80% LLM-made code wherever attributes from the following libraries were used:
            - re
            - ast
            - itertools
            - functools
            - multiprocessing

    - References & Auxiliary Material:
        - `AutoPEP8 <https://pypi.org/project/autopep8/>`_, code formatting;
        - `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_, documentation;
        - `StackOverflow <https://stackoverflow.com>`_, definitions, concepts;
        - `W3Schools <https://w3schools.com/python/>`_, theories, fundamentals, methods;
        - `OpenAI's ChatGPT <https://chat.openai.com>`_, definitions, debugging;
        - `Claude AI <https://claude.ai>`_, additional debugging;
        - `Codeium AI <https://codeium.com>`_, autocompletion, code refactoring & cleaning;
        - `SingleFile <https://chromewebstore.google.com/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle>`_, HTML factoring of this Sphinx-generated documentation;
        - `JetBrains Mono <https://github.com/JetBrains/JetBrainsMono>`_, this :magenta:`awesome` font!

    - Credits & Thanks:
        - A big thanks to my professor `Vitor Tocci <https://br.linkedin.com/in/vitor-tocci-79249164>`_, who lectured `Introduction to Data Proccessing <https://www.ementario.uerj.br/ementa.php?cdg_disciplina=627>`_ and introduced me into Python programming when I had little background experience in the matter.
        - Thanks to my beloved girlfriend :fuchsia:`Ana Caroline`, who tirelessly heard me babble about Python through hours in these past few months where I was still learning and improving much of my understanding of the language. I love you!
        - Thanks to :orange:`all my friends` who helped me debug the documentation itself (this HTML file) when I had zero `Sphinx` knowledge. I hope I did well enough and hope to do much more in the future!

ㅤ

Formatter Functions
-------------------

(Goto :ref:`**PlainTools' Docs**`)

Formatter functions are intended to take a variety of types as input and 
output data in a formatted, previsible way.


.. py:function:: pt.plist(*vals) -> List[Any]:

    Plain List.

    Transforms iterable sets into a flat list; Recursive unpacking.

    :Pseudocode:
        If one (List) contains other (Lists) inside:
            - (Unpack) the (Lists) inside, keeping only the (Values).
        
            This repeats until all (Lists) only contains plain (Values).

        :orange:`Return` a final (List) containing only the (Values) of everything given.

    :Examples:
        plist((1, 2), [3, 4], {5, 6})
            - [1, 2, 3, 4, 5, 6]

        plist({0: 10, 1: 20, 2: 40})
            - [10, 20, 40]

        plist({'A':10, 'B':15, 'C':20, 'D':{"X": 100, "Y": 200, "Z": 300}})
            - [10, 15, 20, 100, 200, 300]

    :Args:
        \*vals: Any | Iterable[Any]
            - Data entries to be flattened.

    :|Returns|:
        R: List[Any]
            - Flat list containing the data entries.


.. py:function:: pt.punit(*its) -> Any | Tuple[Any]:
    
    Plain Units.

    Unpacks single units inside iterable sets;

    Returns a single value if there is only one value in the iterable.

    :Pseudocode:
        If any given (List) contains a (Single) (Value):
            - (Unpack) the (List), so it becomes it's plain (Value).

        If (Final List) contains (Multiple) (Values):
            - :orange:`Return` (Final List).
        
        Else, if (Final List) contains a (Single) (Value):
            - :orange:`Return` (Value).

    :Examples:
        punit([5], [3, 2], [[9]])
            - (5, [3, 2], 9)
        
        punit([1, 2], 3, (4,))
            - ([1, 2], 3, 4)
        
        punit([[7, 8]], {9})
            - ([7, 8], 9)

    :Args:
        \*its: Iterable[Any]
            - Iterable sets.

    :|Returns|:
        R: Any | Tuple[Any]
            - A single item or a tuple of items.


.. py:function:: pt.pnumber(*vals, tol='auto', dcm='auto', prd=4) -> Number | Iterable[Number] | None:

    Plain Number.

    Numeric formatter; Evaluates numeric expressions;
    Removes floating point imprecision errors with great accuracy;
    Works well expressing repeating decimals.
    
    The 'tol' argument is used roughly for the precision of the output.
    It is designed to work 99.9% of the time, figuratively speaking, 
    with a standard precision of up to 1e-12 when set to 'auto', as default.

    The 'dcm' argument works similarly to the 'ndigits' argument found in 
    the 'round()' built-in function, and in fact, is used into it along 
    the works. The default setting of 'auto' will round the number if 
    any repeating decimals are found, up to 4 repetitions.

    :Examples:
        pnumber([8.0, '0.1 * 3', '355/113', 'math.e'])
            - [8, 0.3, 3.1415929203539825, 2.718281828459045]

        pnumber(1/3, 10/33, 100/333, 1000/3333)
            - [0.333, 0.30303, 0.3003003003, 0.3000300030003]
        
        pnumber(0.1 ** 1e-12)
            - 0.9999999999977
        
        pnumber(0.1 ** 32) :gray:`# Fails with 'auto' precision tolerance.`
            - 0 :gray:`# float(0.1 ** 32) is 1.0000000000000018e-32`
        
        pnumber(0.1 ** 32, tol=32)
            - 1e-32

    :Args:
        \*vals: Real | Iterable[Real | String]
            - Numbers to be formatted.
    
    :Kwargs:
        tol: String | Integer = 'auto'
            - Precision of the output;
            - It is recommended to follow the lowest decimal place.
            - i.e. tol=64 for a precision of up to 1e-64.

        dcm: String | Integer = 'auto'
            - Decimal places of the output;
            - It is involved in the rounding phase of the function.
            - 'auto' rounds repeating decimals up to 4 repetitions;
            - i.e. pnumber(1/3, dcm='auto') == 0.3333
            - (dcm=16 | dcm=None) end up with the same result.

    :|Returns|:
        R: Real | Iterable[Real] | None
            - Formatted numbers, None if NaN.


.. py:function:: pt.pdecimals(*nums) -> Integer:

    Plain Decimals.

    Identifies the highest number of decimal places in a set of given numbers.

    :Pseudocode:
        Start (Decimals) as 0.

        (For Each) (Value):
            - If (String) of (Number) in (Value) have ('.') character:
                (Count) how many (Digits) there is after ('.') character.
                    - If (Digits) is greater than (Decimals):
                        (Decimals) become number of (Digits).
        
        :orange:`Return` final (Decimals) value.

    :Examples:
        pdecimals(1.23, 4.5678, 3.1, 5.67890)
            - 4
        
        pdecimals(1/3)
            - 3

        pdecimals(math.pi)
            - 15

    :Args:
        [*]nums: Number | Iterable[Number | String]
            - Numbers to be formatted.

    :|Returns|:
        R: Integer
            - Highest quantity of decimal places found.


.. py:function:: pt.pstring(*objs, sep = ', ') -> String:

    Plain String.

    More comprehensible 'str()' operator; Concatenates elements of iterables.

    :Pseudocode:
        Check (Type) of (Value):
            - If (Type) is (Dictionary):
                (Include) the (Keys) and (Values) of (Dictionary) in the (String).
            - Else, if (Type) is a (List), (Tuple) or (Set):
                (Include) all (Values) in the (String).
            - Else, if (Type) is (Something Else):
                (Include) the String of (Type) in the (String).
        
        :orange:`Return` final version of (String).

    :Examples:
        pstring({0: 'a', 1: 'b', 2: 'c'})
            - '0: a, 1: b, 2: c'
        
        pstring([1, 2, 3], (4, 5), {6, 7})
            - '1, 2, 3, 4, 5, 6, 7'
        
        pstring('Hello', ['world', '!'], sep = ' ')
            - 'Hello world !'

    :Args:
        \*objs: Any | Iterable[Any]
            - Objects to be converted to string.
    
    :Kwargs:
        sep: String = ', '
            - Separator between elements in the final string.

    :|Returns|:
        R: String
            - Single string containing the concatenated elements.    


.. py:function:: pt.pistype(obj, *types) -> Bool | Tuple[Bool]:
    
    Plain Type Check.

    Checks if the object is an instance of the provided types.

    :Pseudocode:
        Check (Type) of (Value) and (Type) of (Asked Types):
            (For Each) (Asked Type):
                - If (Type) of (Value) is the same as this (Asked Type):
                    (Include) (True) in the final (Result)
                - Else, if (Type) of (Value) is not the same as this (Asked Type):
                    (Include) (False) in the final (Result)

        :orange:`Return` the final (Result).

    :Examples:
        pistype('Hello', String, Iterable, Set)
            - (True, True, False)
        
        pistype([1, 2, 3], List, Tuple, Iterable)
            - (True, False, True)
        
        pistype(42.0, Number, Integer, Float)
            - (True, False, True)

    :Args:
        obj: Any
            - Object to be checked against.
        
        \*types: Type
            - Types to compare using isinstance(obj, type).

    :|Returns|:
        R: Bool | Tuple[Bool]
            - Sequence of Booleans according to the checks.


.. py:function:: pt.prange(*args, type = 'list') -> Iterable[Number]:

    Plain Range.

    Simulates the 'range()' function from Python 2.x.

    Instead of a *range* object, returns a plain *Iterable* of specified type.
    
    Stop argument is the de-facto stop, being the last value of list.

    Args functionality is the same as standard 'range()' built-in function.

    :Pseudocode:
        Check for the given (Parameters):
            - If there is (One) (Parameter):
                :orange:`Return` a (List) (Starting) at (0) and (Stopping) at 
                (Parameter) with an (Step) of (1).
            - Else, if there are (Two) (Parameters):
                :orange:`Return` a (List) (Starting) at (1st Parameter) and (Stopping)
                at (2nd Parameter) with a (Step) of (1).
            - Else, if there are (Three) (Parameters):
                :orange:`Return` a (List) (Starting) at (1st Parameter), (Stopping)
                at (2nd Parameter) with a (Step) of (3rd Parameter).
            - Else, if there are (Four) (Parameters):
                :orange:`Return` an (Iterable) of (Type) (4th Parameter),
                (Starting) at (1st Parameter), (Stopping) at
                (2nd Parameter) and with a (Step) of (3rd Parameter).
        
        :orange:`Return` the final (Iterable).

    :Examples:
        prange(5)
            - [0, 1, 2, 3, 4]

        prange(5, 2.5, 0.5, 'tuple')
            - (5, 4.5, 4, 3.5, 3, 2.5)
        
        prange(0, 15, 4, 'dict')
            - {0: 0, 1: 4, 2: 8, 3: 12}

    :Args:
        \*args: Number
            Functionality varies according to arguments:
                - A single parameter determines the `stop`; with `start` of 1.
                - Two parameters determines `start` and `stop`; with `step` of 1.
                - Three parameters determines `start`, `stop` and `step`; returning a `list`.
                - Four parameters determines `start`, `stop`, `step` and `type`

    :Kwargs:
        start: Number = None
            - Start value of the iterable.

        stop: Number = None
            - Stop value of the iterable.

        step: Number = None
            - Step value of the iterable.

        type: String = None
            - Type of the returned iterable ('list', 'tuple', 'set', 'dict', 'cont').

    :|Returns|:
        R: Iterable[Number] = Iterable (defined in 'get') containing the range.


.. py:function:: pt.pinterval(*args, type='list') -> Iterable[Number]:

    Plain Interval.

    Generates a list of numeric elements equidistant between them, from start to stop.

    :Pseudocode:
        Check for the given (Parameters):
            - If there is (One) (Parameter):
                :orange:`Return` a (List) (Starting) at (0) and (Stopping) at
                (100) with (Parameter) (Values).
            - Else, if there are (Two) (Parameters):
                :orange:`Return` a (List) (Starting) at (0) and (Stopping)
                at (2nd Parameter) with (1st Parameter) number of (Values).
            - Else, if there are (Three) (Parameters):
                :orange:`Return` a (List) (Starting) at (2nd Parameter), (Stopping)
                at (3rd Parameter) with (1st Parameter) number of (Values).
            - Else, if there are (Four) (Parameters):
                :orange:`Return` an (Iterable) of (Type) (4th Parameter),
                (Starting) at (2nd Parameter), (Stopping) at
                (3rd Parameter) and with (1st Parameter) number of (Values).

        :orange:`Return` the final (Iterable).

    :Examples:
        pinterval(5)
            - [0, 25, 50, 75, 100]

        pinterval(3, 5)
            - [0, 2.5, 5]

        pinterval(5, 10, 0, 'cont')
            - {0: 10, 1: 7.5, 2: 5, 3: 2.5, 4: 0}

    :Args:
        \*args: Number
            - Can contain up to four positional arguments:
                - One argument: divs;
                    List of [0, 0±n1, 0±n2, (...), 100] with 'divs' elements.
                - Two arguments: divs and stop;
                    List of [0, 0±n1, 0±n2, (...), stop] with 'divs' elements.
                - Three arguments: divs, start and stop;
                    List of [start, start±n1, (...), stop] with 'divs' elems.
                - Four arguments: divs, start, stop and type.
                    Iterable of type(start, (...), stop) with 'divs' elements.

    :Kwargs:
        divs: Number = None
            - Number of elements in the returned Iterable.

        start: Number = None
            - Start value of the interval (default is 0).

        stop: Number = None
            - Stop value of the interval.

        type: String = None
            - Type of the returned collection ('list', 'tuple', 'set', 'dict').

    :|Returns|:
        R: Iterable[Number]
            - List of numeric values with equidistant intervals.


.. py:function:: pt.psequence(*nums, abs_lim = None, rel_lim = 10e3) -> Chain[Real]:

    Plain Sequence.

    Generates a numerical sequence based on the provided numbers or patterns. 
    
    It supports the use of ellipsis (`...`) to denote the continuation 
    of the sequence with a defined step or to an optional limit.

    :Args:
        \*nums: Real | Iterable[Real]
            - The numbers or patterns used to generate the sequence. 
            - Ellipsis (`...`) can be used to sign continuation of sequence.
    
    :Kwargs:
        abs_lim: Real = None
            - The absolute limit for the sequence, if provided.
        
        rel_lim: Real = 10e3
            - The relative limit, as a multiplier to the last expressed num.

    :|Returns|:
        R: Chain[Real]
            - A chain of numbers representing the generated sequence.

    :Example:
        psequence(1, 2, 3, ..., 10)
            - Generates the sequence equivalent to (1, 2, ..., 9, 10).

        psequence(1, 3, 5, ..., abs_lim=150)
            - Generates the sequence equivalent to (1, 3, ..., 147, 149).
        
        psequence(0.1)
            - Generates the sequence equiv. to (0.1, 0.2, ..., 999.9, 1000).
    
    :Notes:
        - If an ellipsis (`...`) is used, the function will infer the step 
          from the preceding numbers in the sequence.
        - If `abs_lim` is provided, the sequence will stop when it reaches 
          or exceeds this limit.
        - If `rel_lim` is provided, it will be used to calculate the maximum 
          limit based on the last number in the sequence before the ellipsis.
        - The sequence continues either until the absolute 
          or relative limit is met.


.. py:function:: pt.pindex(target, *its) -> Integer | None | Tuple[Integer | None]:

    Plain Index.

    Returns the index of the first occurrence of 'target' in 'its'.

    :Pseudocode:
        Look for (Target) in all (Iterables) provided:
            (For Each) (Iterable):
                - If (Target) is found in this (Iterable):
                    (Include) (Target)'s (Index) in the final (Result).
                - Else, if (Target) is not found in this (Iterable):
                    (Include) (None) in the final (Result).

        :orange:`Return` the final (Result).

    :Examples:
        pindex(True, (False, False, True))
            - 2
        
        pindex(5, range(10))
            - 5
        
        pindex(1, (False, False, True), ['a', 'b', 'c'], range(10))
            - (2, None, 1)

    :Args:
        target: Any
            - Value to search for in the provided iterables.

        \*its: Iterable[Any]
            - One or more iterables to be checked for 'target'.
        
    :|Returns|:
        R: Integer | None | Tuple[Integer | None]
            - Index of the first 'target' occurrence into provided iterables.


.. py:function:: pt.pminmax(*vals) -> Container[String: Number]:

    Plain Min & Max.

    Returns the minimum and maximum values from a set of numbers.

    :Pseudocode:
        Given any (Values) or (Iterables[Values]):
            :orange:`Return` both (Minimum) and (Maximum) from all given 
            (Values).

    :Examples:
        pminmax([5, 2, -8, '15*2'])
            - {'min': -8, 'max': 30}

        pminmax([5, 2, -8, '15*2']).min
            - -8

        pminmax(1, -2, ['1.5 * 2'], math.pi)[1][1]
            - 3.141592653589793

    :Args:
        \*vals: Number | Iterable[Number]
            - Objects to be compared for their value.

    :|Returns|:
        R: Container[String: Number]
            - A Container, derived from dict, containing min & max values.


.. py:function:: pt.plen(*iters) -> Container[String: Integer]:

    Plain Length.

    Returns the minimum and maximum sizes of given iterables.

    :Pseudocode:
        Given any (Iterables):
            :orange:`Return` both (Minimum) and (Maximum) (Size) from all given 
            (Iterables).

    :Examples:
        pcount([1, 2, 3], (4, 5), {6})
            - {'min': 1, 'max': 3}

        pcount([1, 2, 3, [4, 5], 6], ("ABCDEFGHIJ", "XYZ"), {}).min
            - 0

        pcount({0: 1, 1: -2, 2: 4, 3: -8, 4: 16, 5: 32}).max
            - 5

    :Args:
        \*iters: Any | Iterable[Any]
            - Objects to be counted for their sizes.

    :|Returns|:
        R: Container[String: Integer]
            - A Container , derived from dict, containing min & max lengths.


.. py:function:: pt.pabs(*nums) -> Container[String: Number]

    Plain Absolutes.

    Identifies the lowest or highest absolute number of a set.
    Returns a Container with the min, max, original min, original max values.

    :Pseudocode:
        (Flatten) the input (Values).
        - Calculate the (Absolute) (Maximum) (Value).
        - Calculate the (Absolute) (Minimum) (Value).
        - Identify the (Original) (Maximum) and (Minimum) (Values).

        :orange:`Return` a (Container) with (Absolute) and (Original) (Minimum) and (Maximum) (Values).

    :Examples:
        x = pabs([5, 8, -2, '15*2'])
            - x == {'min':2, 'max':30, 'ogmin':-2, 'ogmax': 30}
            - x.min == 2
            - x.ogmin == -2
            - x.max == x.ogmax == 30
        
        y = pabs(-1, -2, ['1.5 * 2'], math.pi)
            - y['min'] == 1
            - y['ogmin'] == -2
            - y['max'] == 3.141592653589793
        
        zmin, zmax, ztruemin, ztruemax = pabs(prange(-10, 0, 1))
            - zmin == 0
            - zmax == 10
            - ztruemin == -10
            - ztruemax == 0

    :Args:
        \*nums: Number | Iterable[Number | String]
            - Objects to be counted.

    :|Returns|:
        R: Container[String: Number]
            - A Container, with min, max, original min and original max.


.. py:function:: pt.psum(*nums) -> Real:

    Plain Sum.

    Returns the sum of possible numbers from given sets.

    :Examples:
        psum([5, 2, -8, '15*2'])
            - 29
        
        psum(prange(-10, 0))
            - -55
        
        psum(Container(John=2.55, Maria=3.14, Paul=1.75))
            - 7.44

    :Args:
        \*nums: Real | Iterable[Real | String]
            - Objects to be counted.

    :|Returns|:
        R: Real
            - Sum of numbers.


.. py:function:: pt.pimport(libs, funs = None) -> Module | Object | Tuple[Module | Object]:

    Plain Import.

    Helper function for local scope importation.

    :Pseudocode:
        (Split) (Libs) into individual (Module Names).

        (For Each) (Module Name):
            - Attempt to (Import) the (Module).
                - If (Funs) are given, attempt to (Import) only the specified (Objects) from the (Module).

        :orange:`Return` the (Imported) (Modules) or (Objects) as (Objects).

    :Examples:
        calc = pimport('math')
            - Allocates 'calc' as an alias to the 'math' module.
            - ie: calc.e == math.e

        pi, log = pimport('math','pi, log')
            - Allocates to variables the imported objects (math.pi & math.log).
            - ie: pi == math.pi

    :Args:
        libs: String
            - Modules to import; separated by comma in the 1st string.
            - ('a, b, c').

        funs: String = None
            - Objects to import; separated by comma in the 2nd string.
            - ('a, b, c').

    :|Returns|:
        R: Module | Object | Tuple[Module | Object]
            - Imported modules or objects.


.. py:function:: pt.pframe(depth, outer=False) -> Frame:

    Plain Frame.

    Helper function for getting the frame information in the specified depth.

    :Pseudocode:
        (Inspect) all the current (Frames).

        :orange:`Return` the (Depth)º (Frame), counting from the current (Frame) outwards.

    :Examples:
        (@file PlainTools.py)

        x = pframe()
            - x.f_code.co_filename == '..\\path\\to\\file\\PlainTools.py'
            - x.f_lineno == (Line number of `pframe()` call)
            - x.f_code.co_names == (Tuple of strings of names used in the program)
            - x.f_locals == Current frame's `locals()` dictionary.
            - x.f_globals == Current frame's `globals()` dictionary.

    :Args:
        depth: Integer = 1
            - (Default: 1) How many frames to go in;
            - Note that this is in reverse order, so a depth=2 
            - inspects the currentframe up until currentframe()[-2] 
    
    :Kwargs:
        outer: Bool = False
            - Determines if the Frame is get from inspect.getouterframes()

    :|Returns|:
        R: Frame
            - Frame object.

ㅤ


Statement & Extension Functions
-------------------------------

(Goto :ref:`**PlainTools' Docs**`)

Statement Functions bring new, easy-to-use functions that improve the native, 
standard syntax and built-in functions.


.. py:function:: pt.let(**kwargs) -> Container[Any: Any]:

    Let 'Statement'.
    
    Note: The 'let()' function is unusable inside function definition scopes;
    It is neither a bug nor fixable, but a limitation of the Python language.

    Assigns and evaluates multiple variables in a single function call.
    
    Keep in mind that real assignment happens after the function call ends;
    Doing 'let(x=5, y=10, z=x+y)' raises 'NameError: name 'x' is not defined';
    But doing 'let(x=5, y=10), let(z=x+y)' works just fine.

    :Examples:
        let(x=5, y=10, z=math.pi)
            - (5, 10, 3.141592653589793)
            - x = 5
            - y = 10
            - z = 3.141592653589793

        let(w=Seval('15 ** 5 / 2'))
            - w = 379687.5

    :Kwrgs:
        \*\*kwargs: Any
            - Direct assignments to given kwarg variables.

    :|Returns|:
        R: Container[Any: Any]
            - A Container with the relationed objects assigned.


.. py:function:: pt.const(**kwargs) -> Container[Constant: Any]:

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
            - (2.5, 3.5)
            - x == Constant(2.5)
            - y == Constant(3.5)

        const(z=[0, 1, 1, 2, 3, 5, 8, 13])
            - z == Constant([0, 1, 1, 2, 3, 5, 8, 13])

    :Kwargs:
        \**kwargs: dict
            - Additional constants to assign in the current context.

    :|Returns|:
        R: Container[Constant: Any]
            - A Container with the relationed objects assigned as Constants.


.. py:function:: pt.printnl(*args, **kwargs) -> None:

    New Line Print.

    :Rationale:
        Prints the input with a new line after each prompt.


.. py:function:: pt.printc(*args, fill=' ', **kwargs) -> None:

    Centered Print.

    :Rationale:
        Prints the input centered on the window; Fills with (fill) character.


.. py:function:: pt.showcall(func) -> Function:

    Show Call Information.

    This decorator outputs detailed information about the function 
    call, including the line number, function name, arguments, return 
    value or error, and execution time. It is useful for debugging and 
    monitoring function execution.

    :Example:
        @showcall

        def my_function(x, y):

        ㅤㅤㅤㅤreturn x + y

        - my_function(3, 4)
            - [!-CALL-!]
            - Ln 10 :gray:`# Example!`
            - Fn my_function
            - A* (3, 4)
            - K* {}
            - R* 7
            - Tm 0.0001s
        
        ㅤ

        @showcall

        def vec_func(i, j, k, op='div'):

        ⠀⠀⠀⠀(...)

        ⠀⠀⠀⠀if op == 'div':

        ⠀⠀⠀⠀⠀⠀⠀⠀return (i * j) / k

        - vec_func(2, 3, 0) :gray:`# Division by zero!`
            - [!-CALL-!]
            - Ln 14 :gray:`# Example too!`
            - Fn vec_func
            - A* (2, 3, 0)
            - K* {'op': 'div'}
            - R* [!-ERROR-!]
            - Er ZeroDivisionError
            - As division by zero
            - Tm 0.017s

.. py:function:: pt.doc(*objs) -> List[String] | Null:

    Docstring Printer.

    :Rationale:
        Prints into the console any docstring associated with the given 
        object(s) or its parent class(es), headed by its origin module.
        
        Prints the current frame's module docstring if no object is given.

.. py:function:: pt.skip(n=1, *args, **kwargs) -> None:

    Line Skip.

    :Rationale:
        Prints into de console 'n' times; Defaults to a 1 line skip.


.. py:function:: pt.evinput(*args, **kwargs) -> None:

    Evaluated Input.

    :Rationale:
        Performs a Safe Eval (see: Seval@:ref:`Instantiable Classes`) 
        into the input, converting to adequate types.


.. py:function:: pt.timeout(secs, func, *args, **kwargs) -> Any | Error:

    Timeout.

    Runs a function in a separate proccess with a time limit;
    Raises an exception if it exceeds given limit in seconds.

    :Examples:
        timeout(5, long_running_function, arg1, arg2)
            - Executes long_running_function(arg1, arg2) with a 5-second limit.

    :Args:
        secs: Number
            - Time limit in seconds.

        func: Callable
            - Function to execute.

        \*args: Any
            - Positional arguments to pass to the function.

        \*\*kwargs: Any
            - Keyword arguments to pass to the function.

    :|Returns|:
        R: Any | Err
            - The result of the function, or an exception if timed out.


.. py:function:: pt.loop(times=0, escape=KeyboardInterrupt, loopif=True, show=False, nl=False) -> Decorator:

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

        ⠀⠀⠀⠀print(f"Value: {x}")

        - This will print the value of `x` three times at 'my_function()'.

        ㅤ

        @loop(loopif=lambda: some_condition())

        def my_function(x):

        ⠀⠀⠀⠀print(f"Value: {x}")

        - This will execute `my_function` as long as `some_condition()` returns True.

        ㅤ

        @loop(escape=KeyboardInterrupt)

        def my_function(x):

        ⠀⠀⠀⠀print(f"Processing {x}")

        - This will execute `my_function` in a loop until a `KeyboardInterrupt` exception is raised.

        ㅤ

        @loop(times=5, show=True)

        def example_function(x):

        ⠀⠀⠀⠀print(x)

        - This will run 'example_function()' 5 times, printing the iteration details each time.

    :Args:
        times: Integer = 0
            - The number of times to execute the decorated function. 
            - If set to 0, the loop will run indefinitely unless broken out.
            - Default is 0.

        escape: Exception | Tuple[Exception, ...] = KeyboardInterrupt
            - Exception(s) that, if raised, will stop the loop.
            - Default is KeyboardInterrupt (guaranteed even if changed).

        loopif: Function | Bool = True
            - A condition that, if evaluated to False, will break the loop.
            - It can be a Lambda type with out-scope parameters or conditions. 
            - Default is True.

        show: Bool = False
            - If True, prints the function name, arguments, and iteration. 
            - Default is False.
            
        nl: Bool = False
            - If True, inserts a newline after each iteration.
            - Default is False.

    :|Returns|:
        Decorator
            - A decorator that wraps the provided function.


Debugger & Utility Functions
----------------------------

(Goto :ref:`**PlainTools' Docs**`)

Debug functions interact with the environment the script runs in, 
and output relevant information to the console.

These functions do accept arguments only as buffers, this being,
arguments given have no impact in the output, but serve the purpose of
executing code in the same line, such as starting a timer for example.


.. py:function:: pt.debug(*buffer) -> List[String] | None:

    Debug Traceback.
    
    :Examples:
        - Try: (...)
        - Except: printnl(\*debug())

    :Rationale:
        Returns the traceback, if any.


.. py:function:: pt.clear(*buffer) -> None:

    Clear Screen.

    :Rationale:
        Simple command to clear the console feed.


.. py:function:: pt.eof(*buffer) -> SystemExit:

    End of File.

    :Rationale:
        Logs into a .log file, waits for user input, and then exits the system.


.. py:function:: pt.deepframe(*buffer) -> None:

    Deep Frame.

    :Rationale:
        Prints the full depth of the current path and the frame stack.

ㅤ


Operator & Instantiated Classes
-------------------------------

(Goto :ref:`**PlainTools' Docs**`)

Operator Classes are classes able to be used as functions, objects, contexts 
and as the name sugests, come with pre-loaded instances that are ready-to-use.

The class definition for these objects is given in UPPERCASE, as in:
    - class TIME:
        (...)

Where the instances are given in PascalCase, as is with other non-operator classes, so:
    - Time = TIME(std='now')
    - Runtime = TIME(std='lap')
    - Crono = TIME(std='epoch')

Are all instance examples of the operator class 'TIME()'


.. py:class:: pt.TIME

    Execution Timer.

    A running timer that starts immediately when instantiated.

    :Examples:
        X = TIME()
            - Starts 'X' as a timer.

        with X:
            - Starts a timed context with 'X'; prints time on exit.

        X.show
            - Prints the current time in string format.

    :Args:
        add: Float = 0.0
            - Time to add to the timer.

        std: String = 'now'
            - Initial standard mode ('now', 'lap', or 'epoch').

    :Methods:
        .mode(std: String = '') -> Class
            - Changes the standard mode of the timer.

        .now -> Float
            - Returns the time since the last call.

        .lap -> Float
            - Returns the current time.

        .reset -> Class
            - Resets the timer.

        .string -> String
            - Returns the time as a string.

        .show -> String
            - Prints the current time in string format.

        .epoch -> List[Float]
            - Returns recorded times.

    :Instances:
        Time = TIME(std='now')
            - Timer that returns the time since the last call.
            
        Runtime = TIME(std='lap')
            - Timer that returns the total elapsed time.
            
        Crono = TIME(std='epoch')
            - Timer that returns the entire history of recorded times.

    :|Returns|:
        R: Float | List[Float]
            - Time in seconds.milliseconds (e.g. 1.234).


.. py:class:: pt.STUB

    Decorator @Stub | Object Stub.

    Decorates an incomplete function, indicating it has not been implemented yet.

    :Examples:
        @Stub
            - Prints the stub location when the function is called.

        Stub()
            - Prints the stub status, current line and module of call.

        Stub
            - Null object with empty representation.
    
    :Instances:
        Stub = STUB()

    :|Returns|:
        R: Class | Callable
            - Decorated function or Stub object.


.. py:class:: pt.NULL

    Null Object Pattern.

    A class that implements the Null Object Pattern by defining methods and operations that return neutral values or perform no actions.

    :Examples:
        Null()
            - Returns an instance of the NULL class.

        Null + 5
            - Performs a no-op and returns Null itself.
            - Null

        str(Null)
            - Returns an empty string.
            - ''

        Null.attribute
            - Accesses a non-existent attribute, returns Null.
            - Null
    
    :Instances:
        Null = NULL()

    :|Returns|:
        R: Class | Any
            - Returns neutral values or the instance itself, depending on the operation.


.. py:class:: pt.ERROR(NULL)

    Error Object.

    A specialized version of the 'NULL' class that represents an error state, 
    overriding string and representation methods to return 'Error'.

    :Examples:
        str(Error)
            - 'Error'

    :Instances:
        Error = ERROR()

    :|Returns|:
        R: String
            - Always returns the string 'Error' for both string and representation methods.


.. py:class:: pt.MAIN

    Main script guard.

    Evaluates if the script is being executed directly; 
    Similar to __name__ == '__main__'.

    :Examples:
        if Main:
            - Evaluates if __name__ == '__main__'.

        with Main:
            - Enters the 'Main' context, only executes if Main.

        Main(\*args, \*\*kwargs)
            - Invokes the 'Main' context; runs local 'main(\*args, \*\*kwargs)'.
            - main(\*args, \*\*kwargs) :gray:`# Inside 'with Main:' context.`

    :Methods:
        .time -> Float
            - Returns the script execution time.

        .showtime -> String
            - Displays the script execution time.

        .clear -> Self
            - Clears the console; Executed by .start.

        .start -> Self
            - Invokes .time & .clear.

        .end -> Self
            - Ends the program after debugging and logging.
    
    :Instances:
        Main = MAIN()

    :|Returns|:
        R: Bool = True if the script is being executed directly.


.. py:class:: pt.SILENCE

    Context manager that suppresses console output.

    Redirects stdout and stderr to /dev/null, effectively silencing 
    all output within the context.

    :Examples:
        with Silence:
            - Silences all console output within the context.

    :Instances:
        Silence = SILENCE()

    :|Returns|:
        R: Class = Context manager that suppresses console output.


.. py:class:: pt.LOGGING

    Functional Logging.

    Stores provided strings or objects in an internal list; 
    Writes them to a (filename).log file.

    :Examples:
        Logging("message")
            - Logs "message" in the internal list.

        Logging([1, 2, 3])
            - Logs each element of the list on separate lines.

    :Args:
        obj: Any
            - Object(s) to be logged.

    :Methods:
        .get -> List
            - Returns the internal list of logged entries.

        .flush -> Self
            - Writes the current log to a file and clears the internal list.
            - This is automatically done at exiting the 'with Main' context.

        .show -> Self
            - Displays the stored messages from the log list.

        .reset -> list or None
            - Resets the internal list of logs to empty.

    :Instances:
        Logging = LOGGING()


.. py:class:: pt.TRY

    Try Context.

    A simpler 'try' context, with no direct error handling; Exits the context instead.

    Can be done in a verbose way by the use of 'with Try.show:' method.

    :Examples:
        with Try:
            - Begins execution and tracks its success or failure.

    :Methods:
        .show -> Self
            - Enables verbose mode to print the context's progress and results.

    :Properties:
        verbose: Bool = False
            - Controls whether to print the result to the console.
        
        result: String
            - Stores the result of the try block, indicating success or failure.


.. py:class:: pt.LINES

    Line Number Context Manager.

    A context manager that prefixes each line of output with the line number.

    :Examples:
        with Lines:
            - print("Hello, World!")  :gray:`# Output will be prefixed with line no.`
    
    :Instances:
        Lines = LINES()


.. py:class:: pt.SEVAL

    Safe Expression Evaluator.

    A secure alternative to Python's `eval()` function, designed to evaluate
    mathematical and basic expressions while preventing access to unsafe 
    operations and functions.

    :Examples:
        Seval("2 + 2")
            - 4

        Seval("round(math.pi * 2, 2)")
            - 6.28 :gray:`# Only if 'math' is imported in the current namespace.`
        
        Seval(""import shutil; shutil.rmtree('/.')")
            - Raises UnsafeError.

    :Raises:
        UnsafeError: Raised when tries unsafe operation, function, or module.
    
    :Attributes:
        UnsafeError: TypeError
            - Custom error for handling unsafe operations.

        blacklist: dict
            - Defines disallowed functions and modules that are prohibited.

ㅤ


Constructor Classes & Custom Objects
------------------------------------

(Goto :ref:`**PlainTools' Docs**`)

Constructor Classes have the purpose of creating Custom Objects that can be
manipulated in specific, useful ways. There is a variety of Custom Objects 
introduced in the module, so a more in-depth explanation is provided in 
each's documentation below.


.. py:class:: pt.Container

    Container Class; dict Subclass.

    Note: Containers can't have numeric keys due to how their keys are 
    directly associated to its instance attributes. However, any String 
    type is a valid key type. Attempting to update a Container instance 
    with enumerated dictionaries will raise a TypeError.

    A flexible dictionary-like container class that supports various 
    operations and transformations. Unlike a standard dictionary, 
    a `Container` is unpacked by its values rather than by its keys.
    
    The Container supports basic arithmetic operations on a per-key basis, 
    meaning that you can operate an iterable to a Container, where each 
    ordered element operates each key's value until exhaustion; Where as 
    single, non-iterable operations are performed on the entire Container.
    
    Containers can have its values accessed as attributes when calling for 
    their keys. This means that assigned attributes into this class are also 
    added to the Container's keys with the designated value.

    :Example:
        C1 = Container(a=1, b=2)  
            - Creates a Container as {'a': 1, 'b': 2}

        C2 = Container('c')
            - Creates a Container as {'c': None}
        
        C1(C2) :gray:`# Same as C1 += C2`
            - Aggregates C1 and C2 for {'a': 1, 'b': 2, 'c': None}
        
        C1.fill(4)
            - Alocates '4' to the first encounter of `None` value in C1.

    :Methods:
        .sort(\*args, \*\*kwargs): Self
            - Sorts the keys (or values) of the Container; Optional lambda.
            
        .shove(\*vals): Self
            - Adds the values to the keys following the current order of keys.
        
        .fill(\*vals, target=None, exhaust=True): Self
            - Fills in any `target` vals in the Container with provided vals.
            - `target` argument can be a lambda|function|builtin|singleton.
            - `exhaust` argument defines if fill is finite or cyclic infinite.
        
        .order(\*keys): Self
            - Orders the keys of the Container as provided.
        
        .only(\*keys): Self
            - Returns a Container containing only the specified keys.
        
        .without(\*keys): Self
            - Returns a Container without the specified keys.
        
        .keyval(): dict
            - Returns a copy of the dictionary object as {keys: values}.
        
        .key(\*keys): list
            - Returns a list of keys in Container; Optional filter for values.
        
        .val(\*vals): list
            - Returns a list of values in Container; Optional filter for keys.
        
        .sub(): Tuple[Container]
            - Returns a tuple of each k: v pair in Container, as Containers.
        
        .copy(): Container
            - Returns a deepcopy of the current Container.
        
    :Operators:
        Any basic arithmetic operator is supported as in:

        Container <> Container;

        Container <> other (if the operation(value, other) is valid).
        
        Operations with non-iterables are valid as long as the operation to every Container[N] <> other is valid for all given N.
            - i.e. Container(f=1, g=2, h=3) * 2 == Container(f=2, g=4, h=6)
            - i.e. Container(Bob='Foo') - 5 == Container(Bob='Foo', Bob_1=5)
        
        Operations with iterables are valid as long as the operation to every pair Container[N] <> other[N] is valid for the max possible N.
            - i.e. Container(R=5, S=10) * (2,3,4) == Container(R=10, S=30)
            - i.e. Container(T=2,U=4,V=6) - {2,3} == Container(T=0, U=1, V=6)
        
        Remainder of Container <> Other operations are ignored, as the result is a Container type with the same keys as the involved Container.
            - i.e. Container(i=2, j=3) * [2, 3, 4] == Container(i=4, j=9)
        
        Remainer of Container <> Container operations aggregate non-similar keys into the final result, unmodified, as no C1[K] <> C2[K] is valid.
            - i.e. Container(f=5) - Container(g=10) == Container(f=5, g=10)
        
        add (+)
            - Adds the values of another Container, or from a sequence.
            - i.e. Container(a=5) + (b=4) == Container(a=5, b=4)
            - i.e. Container(a=5, b=4) + [3, 4] == Container(a=8, b=8)
        
        sub (-)
            - Subtracts the values of another Container or from a sequence.
            - i.e. Container(x=5, y=10) - 3 == Container(x=2, y=7)
            - i.e. Container(a=5, b=4) - Container(c=3, d=2)
        
        mul (*)
            - Multiplies the values of another Container or from a sequence.
            - i.e. Container(x=5) * 2 == Container(x=10)
            - i.e. Container(x=5, y=4) * (3, 4) == Container(x=15, y=16)
        
        truediv (/)
            - Divides the values of another Container or from a sequence.
            - i.e.Container(T=2,U=4,V=6)/[1,2,3]==Container(T=2.0,U=2.0,V=2.0)
            
        floordiv (//)
            - Floor divides the values of another Cont. or from a sequence.
            - i.e. Container(A=12.5) // Container(A=3.5) == Container(A=3.0)
        
        mod (%)
            - Modulo operates on the values of another Cont. or from a seq.
            - i.e. Container(B=7.5) % Container(B=2) == Container(B=1.5)
        
        pow (**)
            - Raises the values of the Container to the power of.
            - i.e. Container(C=5) ** Container(C=3) == Container(C=125)


.. py:class:: pt.Constant

    Immutable Constants.

    Wraps a value and provides a constant, immutable interface to it.

    Overrides most of the standard dunder methods to ensure immutability.

    Non-dunder methods can be called, but will only return the Constant's 
    value and won't modify the Constant itself or it's value in any way.

    :Examples:
        x = Constant(5)
            - Create an immutable constant with a value of 5
            - i.e. x + 5 == 10
            - i.e. x += 5 ; x == 5

        pi = Constant(math.pi)
            - Assign 'math.pi' to 'pi' as an immutable constant
            - i.e. const(rpi=pi*2) :gray:`# 'rpi' is also a Constant now.`

    :Args:
        value: Any
          - The value to be wrapped as a Constant.

    :|Returns|:
        Constant
          - An immutable Constant instance wrapping the provided value.

ㅤ

ㅤ



**BETA RELEASE V1.0.240902b, WORK IN PROGRESS!**
---------------------------------------------------