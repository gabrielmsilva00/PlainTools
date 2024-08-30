.. figure:: pthead.png
    :scale: 100%
    :height: 252px

    Version\: 1.0.240830b (As in: Main.sub.YYMMDDbranch)


- `Library's Documentation <https://gabrielmsilva00.github.io/PlainTools/>`_
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

You see, :emphasis:`round()` itself is *black-&-white*, in the sense that it 
does what its :emphasis:`ndigits` argument asks it to: round for `n` digits.

