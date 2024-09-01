.. figure:: pthead.png
    :scale: 100%
    :height: 252px

    Version\: 1.0.240830 beta (As in: Main.sub.YYMMDD branch)


- `Library's Documentation <https://gabrielmsilva00.github.io/PlainTools/>`_
    .. figure:: ptqr.png
        :scale: 100%
        :height: 128
        
- `Author's Github <https://github.com/gabrielmsilva00>`_

Introduction
************

Welcome to the PlainTools library's GitHub repo!

PlainTools is a Python 3 library designed to introduce new features and 
fix awkward common interactions present in the Python 3 native ecosystem.

The simplest, yet most relevant example can be:

.. code-block:: python

    >>> import PlainTools as pt

    >>> print(0.1 * 3)
    0.30000000000000004

    >>> print(pt.pnumber(0.1 * 3))
    0.3

Simple, right?

You might be thinking "Oh well, a simple rounding function, how quaint..." (\\s),
but that is far from it!

You see, **round()** itself is *black-&-white*, in the sense that it 
does what its **ndigits** argument asks it to: round for **n digits**. 
So consider the following case:

.. code-block:: python

    >>> def sround(num):
            return round(num, 3)
    
    >>> print(sround(0.1 * 3))
    0.3

Great! Crisis averted. All is well, and we no longer have to deal with pesky 
**float imprecision** anymore!

Hold on, what if you are dealing with small, high precision operations?

"Add more 'ndigits' to round()"

But what about really small, precise float number operat--

"More 'ndigits'!"

But what if--

"MOAR!"


Well, you see, **float imprecision cases** tends to appear more and more the 
smaller the numbers you are dealing with. And sometimes, when you have to do 
a large chain of operations on these small numbers, you will end up with a 
much less precise end result than what y

