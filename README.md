|![Image](https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/pthead.png)
|:-:|
<a href=https://pypi.org/project/PlainTools><img src="https://img.shields.io/pypi/v/plaintools.svg?logo=pypi" alt="Version" width=256 style="vertical-align:middle;margin:5px"><br/><a href=https://github.com/gabrielmsilva00/PlainTools><img src="https://img.shields.io/badge/GitHub-Repository-2A3746?logo=github" width=256 style="vertical-align:middle;margin:5px"><br/><a href=https://github.com/gabrielmsilva00/PlainTools/releases><img src="https://img.shields.io/pypi/dm/plaintools?logo=pypi" alt="Version" width=256 style="vertical-align:middle;margin:5px">
[<img src=https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/ptqrdoc.png?>](https://gabrielmsilva00.github.io/PlainTools)<br/><a href=https://github.com/gabrielmsilva00/PlainTools/actions/workflows/pages/pages-build-deployment><img src="https://github.com/gabrielmsilva00/PlainTools/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main" width=256>

## Installation

This package is **Python 3.11+** compatible and can be installed & upgraded using `pip`:

```sh
pip install -U plaintools
```

The latest release and its changelog can also be found [here.](https://github.com/gabrielmsilva00/PlainTools/releases)

---
## Introduction

**PlainTools is a Python 3.11+ library** designed to introduce new features and 
fix awkward common interactions present in the Python native ecosystem.

Most functions are prefixed with `p` (as in `pt.plist` or `pt.pround`) 
to avoid homonyms. The `p` stands for `Plain` and are the namesake of this package.

---
## Examples

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
0.999999999999123 # No loss of precision up to 15 literal digits.
؜

>>> 0.00000000001 ** 3
9.999999999999999e-34

>>> pt.pnumber(0.00000000001 ** 3)
1e-33 # Corrects scientific-notated float imprecisions as well.
؜

>>> pt.pnumber("math.pi") # A safe variation of 'eval()' is used, as shown below!
3.14159265358979

# https://stackoverflow.com/a/1933463/26469850
>>> pt.pnumber("import shutil; shutil.rmtree('/.')") # Example of malicious use.
PlainTools.SEVAL.UnsafeError: Invalid syntax in expression
؜
```

- More about [Seval (Safe Eval)](https://gabrielmsilva00.github.io/PlainTools/#pt.SEVAL).

Simple, right?

Countless more examples can be found in the [Library's Documentation Page](https://gabrielmsilva00.github.io/PlainTools), so please check it out!

---
## [Resources & Credits](https://gabrielmsilva00.github.io/PlainTools#resources-credits)

This project would be ***impossible*** to make without the **support of my friends and family** around me.

**Thank you everyone.**

- Credits & Thanks:
    - A big thanks to my professor [Vitor Tocci](https://br.linkedin.com/in/vitor-tocci-79249164), who lectured [`Introduction to Data Proccessing`](https://www.ementario.uerj.br/ementa.php?cdg_disciplina=627) and introduced me into Python programming when I had little background experience in the matter.
    - Thanks to my beloved girlfriend **Ana Caroline**, who tirelessly heard me babble about Python through hours in these past few months where I was still learning and improving much of my understanding of the language. I love you!
    - Thanks to **all of my friends and family**, including **@CherryGM** who helped me revise this documentation and greatly encouraged me. And to everyone who helped me debug this documentation itself when I had zero `Sphinx` knowledge. I hope I did well enough and hope to do much more in the future!

؜

- Disclaimer: **LLM (AI) Use**:
    - [ChatGPT](https://chat.openai.com), [Codeium](https://codeium.com) and [Gemini](https://gemini.google.com) (The later not credited as it did not "contribute" directly to the codebase) were used in this project development.
    - **If you, your university or your company (in general, if the target for this library's use) does have any restrictions, implicit or explicit, against the use of LLMs in production | academic coding, please avert from using this library.**
    - Any code "contributed" by or taken from *any* LLM (AI) use, prompted directly or indirectly, was heavily debugged and tested *(to the best of my personal capacity)*. You will probably find **40~80% LLM-made code**** wherever attributes from the following libraries were used:
        - **re**
        - **ast**
        - itertools
        - functools
        - multiprocessing
    - If any code comes across as sluggish, unnoptimized or just bad, please let me know by [raising an issue](https://github.com/gabrielmsilva00/PlainTools/issues) or DMing me at [GitHub @gabrielmsilva00](https://github.com/gabrielmsilva00), or by emailing me at [gabrielmaia.silva00@gmail.com](mailto:gabrielmaia.silva00@gmail.com?subject=PlainTools%20Python%20Library%20Feedback).

؜

- References & Auxiliary Material:
    - [AutoPEP8](https://pypi.org/project/autopep8/), code formatting;
    - [Sphinx](https://www.sphinx-doc.org/en/master/index.html), documentation;
    - [Sphinx-Design](https://sphinx-design.readthedocs.io/en/latest/index.html), styling;
    - [StackOverflow](https://stackoverflow.com), definitions, concepts;
    - [W3Schools](https://w3schools.com/python/), theories, fundamentals, methods;
    - [OpenAI's ChatGPT](https://chat.openai.com), definitions, debugging;
    - [Claude AI](https://claude.ai), additional debugging;
    - [Codeium AI](https://codeium.com), autocompletion, code refactoring & cleaning;
    - [SingleFile](https://chromewebstore.google.com/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle) & [SingleFile CLI](https://github.com/gildas-lormeau/single-file-cli), HTML refactoring of this Sphinx-generated documentation;
    - [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono), this **awesome** font!

؜

| <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" width=256 style="vertical-align:middle;margin:5px">
|:-:|
|<a href=https://github.com/gabrielmsilva00><img src="https://img.shields.io/badge/GitHub-Author-526E8C?logo=github" width=256 style="vertical-align:middle;margin:5px">
| <img src=https://raw.githubusercontent.com/gabrielmsilva00/PlainTools/refs/heads/main/imgs/pttail.png style="vertical-align:middle">