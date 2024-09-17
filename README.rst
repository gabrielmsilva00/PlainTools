.. figure:: pthead.png
    :scale: 100%
    :height: 252px

    Version\: 1.0.240902 beta (As in: Main.sub.YYMMDD branch)


- `Library's Documentation <https://gabrielmsilva00.github.io/PlainTools/>`_

    .. image:: ptqrdoc.png
        :scale: 100%
        :target: https://gabrielmsilva00.github.io/PlainTools/

- `Author's Github <https://github.com/gabrielmsilva00>`_

- `Currently Working on: '@arithmetic' decorator; 'Number' class <https://github.com/gabrielmsilva00/PlainTools/deployments>`_

Introduction
************

Welcome to the PlainTools library's GitHub repo!

PlainTools is a Python 3 library designed to introduce new features and 
fix awkward common interactions present in the Python 3 native ecosystem.

Some simple, yet relevant examples are:

.. code-block:: python

    >>> import PlainTools as pt

    >>> print(0.1 * 3)
    0.30000000000000004

    >>> print(pt.number(0.1 * 3))
    0.3 # Deals with float imprecision errors.

    >>> print(5 / 3)
    1.6666666666666667

    >>> print(pt.number("5 / 3"))
    1.666... # '...' present only in string format; The true value is still float(5/3).

    >>> print(7 / 53)
    0.0958904109589041

    >>> print(pt.number(7 / 53))
    0.095890410958904109589041... # Can detect long chains of repeating decimals!

    >>> print(0.9999999999999988)
    0.9999999999999988

    >>> print(pt.number(0.9999999999999988))
    0.9999999999999988 # No loss of precision up to 15 digits!

    >>> print(pt.number("math.pi")) # A safe variation of 'eval()' is used, as shown below!
    3.141592653589793

    # https://stackoverflow.com/a/1933463/26469850
    >>> print(pt.number("import shutil; shutil.rmtree('/.')")) # Example of malicious use.
    PlainTools.SEVAL.UnsafeError: Invalid syntax in expression

- More about Seval (Safe Eval) can be found at:
  `Plain Tools: Safe Eval <https://gabrielmsilva00.github.io/PlainTools/#pt.SEVAL>`_

Simple, right?

**GitHub Repo|Pages & Documentation is yet Work in Progress!! Thanks for your attention!**
==========================================================================================

.. You might be thinking "Oh well, a simple rounding function, how quaint..." (\\s),
.. but that is far from it!

.. You see, **round()** itself is *black-&-white*, in the sense that it 
.. does what its **ndigits** argument asks it to: round for **n digits**. 
.. So consider the following case:

.. .. code-block:: python

..     >>> def sround(num):
..             return round(num, 3)
    
..     >>> print(sround(0.1 * 3))
..     0.3

.. Great! Crisis averted. All is well, and we no longer have to deal with pesky 
.. **float imprecision** anymore!

.. Hold on, what if you are dealing with small, high precision operations?

.. "Add more 'ndigits' to round()"

.. But what about really small, precise float number operat--

.. "More 'ndigits'!"

.. But what if--

.. "MOAR!"


.. Well, you see, **float imprecision cases** tends to appear more and more the 
.. smaller the numbers you are dealing with. And sometimes, when you have to do 
.. a large chain of operations on these small numbers, you will end up with a 
.. much less precise end result than what y

