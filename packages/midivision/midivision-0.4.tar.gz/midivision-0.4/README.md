# midivision

<!-- This are visual tags that you may add to your package at the beginning with useful information on your package --> 
[![version](https://img.shields.io/pypi/v/midivision?color=blue)](https://pypi.org/project/midivision/)
[![downloads](https://img.shields.io/pypi/dw/midivision)](https://pypi.org/project/midivision/)

Brings basic function related to division in python and relation between the two numbers to divide


<p align="center"><img src="https://img.freepik.com/free-vector/hand-drawn-bernie-cat-sticker-collection_52683-63603.jpg?w=740&t=st=1684435499~exp=1684436099~hmac=f78fe3f68a22b96165839db1844af5fe3b3f40028b0a2e345587229b6ae3efa2" alt="Logo""/></p>

## Download and install


If you are using `PyPI` run the following promt in terminal:

```
pip install pydivision
```

You can also test the unstable version of the package with:

```
pip install -i https://test.pypi.org/simple/ pydivision
```

## Quick start

The package contains functions to make a division, check if two numbers are divisible and ...

For instance:

```
import midivision
print(midivision.division(1,2))  #0.5
```

## Code examples

#### division

    Return the division between two numbers

    Args:
    -    a : Numerator
    -    b : Denominator
        type_ (, optional): Type of result, possible values are "complex","str","int" and "float". Defaults to float.

    Returns:
    -    a/b: Result of division in expected type
    
For instance:

```
import midivision
print(midivision.division(1,2,"complex")) $0.5 + 0j
```

#### isdivisble

    Args:
        a : Numerator
        b : Denominator

    Returns:
        True if a is divisible by b, else False

For instance:

```
import midivision
print(midivision.isdivisible(5,5)) # True
```

What's new:

- Update Image 

-Version 0.4:

- Typo Correct

Version 0.3:

- Update Impage

Version 0.2:

- Functions `division` and  `isdivisible`  was implemented.

Version 0.1:

- First version of the package.

------------

This package has been designed and written by Diego Acosta (C) 2023