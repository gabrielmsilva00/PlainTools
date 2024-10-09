|![Image](https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/pthead.png)
|:--:|
**[Version: 1.2.241008.1](https://github.com/gabrielmsilva00/PlainTools/releases) <br/> (Main.sub.YYMMDD.rev)**
| - [GitHub Repo](https://github.com/gabrielmsilva00/PlainTools) \| [PyPi Repo](https://pypi.org/project/PlainTools)
| - [Author's GitHub Profile](https://github.com/gabrielmsilva00)
[<img src="https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/ptqrdoc.png?">](https://gabrielmsilva00.github.io/PlainTools)

# Installation

This package can be installed & upgraded using `pip`:

```sh
pip install -U plaintools
```

# Introduction

PlainTools is a Python 3 library designed to introduce new features and 
fix awkward common interactions present in the Python 3 native ecosystem.

Most functions are prefixed with `p` (as in `pt.plist` or `pt.pround`) 
to avoid homonyms. The `p` stands for `Plain` and are the namesake of this package.

Some simple, yet relevant examples using the **Plain Number**(`pt.pnumber`) function are:

```python
>>> import PlainTools as pt

>>> 0.1 * 3
0.30000000000000004

>>> pt.pnumber(0.1 * 3)
0.3 # Deals with float imprecision errors.
؜

>>> 5 / 3
1.6666666666666667

>>> pt.pnumber("5 / 3")
1.666... # '...' present only in string format; The true value is still float(5/3).
؜

>>> 1 / 73
0.0136986301369863

>>> pt.pnumber(1 / 73)
0.013698630136986301369863... # Can detect long chains of repeating decimals!
؜

>>> 0.9999999999999988
0.9999999999999988

>>> pt.pnumber(0.9999999999991234)
0.99999999999912 # No loss of precision up to 14 literal digits.
؜

>>> 0.00000000001 ** 3
9.999999999999999e-34

>>> pt.pnumber(0.00000000001 ** 3)
1e-33 # Corrects scientific-notated float imprecisions as well.
؜

>>> pt.pnumber("math.pi") # A safe variation of 'eval()' is used, as shown below!
3.141592653589793

# https://stackoverflow.com/a/1933463/26469850
>>> pt.pnumber("import shutil; shutil.rmtree('/.')") # Example of malicious use.
PlainTools.SEVAL.UnsafeError: Invalid syntax in expression
؜
```

- More about [Seval (Safe Eval)](https://gabrielmsilva00.github.io/PlainTools/#pt.SEVAL).

Simple, right?

Countless more examples can be found in the [Library's Documentation Page](https://gabrielmsilva00.github.io/PlainTools), so please check it out!

| **GitHub Repo & Pages is a constant WIP!!** |
|-|
| **Thank you for your attention!** |