<style>
red { color: Red }
blu { color: Blue }
grn { color: Green }
ylw { color: Yellow }
org { color: Orange }
mgt { color: Magenta }
gry { color: Gray }
</style>

![Image](https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/pthead.png)

> Version\: 1.1.240919 (As in: Main.sub.YYMMDD)


- [Library's Documentation](https://gabrielmsilva00.github.io/PlainTools)

[<img src="https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/ptqrdoc.png">](https://gabrielmsilva00.github.io/PlainTools)

- [Author's Github](https://github.com/gabrielmsilva00)

# Installation

This package can be installed using <org>`pip`</org> in your CLI of choice as:

```
pip install PlainTools
```

The PyPi page can be found [here.](https://pypi.org/project/PlainTools/)

# Introduction

Welcome to the PlainTools library's GitHub repo!

PlainTools is a Python 3 library designed to introduce new features and 
fix awkward common interactions present in the Python 3 native ecosystem.

Most functions are prefixed with <org>`p`</org> (as in `pt.plist` or `pt.pround`) 
to avoid homonyms. The <org>`p`</org> stands for <org>`Plain`</org> and are the 
namesake of this package.

Some simple, yet relevant examples using the <org>**Plain Number**</org>
(<org>`pt.pnumber()`</org>) function are:

```python
>>> import PlainTools as pt

>>> print(0.1 * 3)
0.30000000000000004

>>> print(pt.pnumber(0.1 * 3))
0.3 # Deals with float imprecision errors.
؜

>>> print(5 / 3)
1.6666666666666667

>>> print(pt.pnumber("5 / 3"))
1.666... # '...' present only in string format; The true value is still float(5/3).
؜

>>> print(7 / 53)
0.0958904109589041

>>> print(pt.pnumber(7 / 53))
0.095890410958904109589041... # Can detect long chains of repeating decimals!
؜

>>> print(0.9999999999999988)
0.9999999999999988

>>> print(pt.pnumber(0.9999999999999988))
0.9999999999999988 # No loss of precision up to 15 literal digits.
؜

>>> print(0.00000000001 ** 3)
9.999999999999999e-34

>>> print(pt.pnumber(0.00000000001 ** 3))
1e-33 # Corrects scientific-notated float imprecisions as well.
؜

>>> print(pt.pnumber("math.pi")) # A safe variation of 'eval()' is used, as shown below!
3.141592653589793

# https://stackoverflow.com/a/1933463/26469850
>>> print(pt.pnumber("import shutil; shutil.rmtree('/.')")) # Example of malicious use.
PlainTools.SEVAL.UnsafeError: Invalid syntax in expression
؜
```

- More about [Seval (Safe Eval)](https://gabrielmsilva00.github.io/PlainTools/#pt.SEVAL).

Simple, right?

## GitHub Repo|Pages is yet WIP!! Thanks for your attention!**
---