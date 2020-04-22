# resf - Result Formatter

A simple package for displaying calculation results in a textbased table

## Install

```python
pip install resf
```

[pypi page](https://pypi.org/project/resf/)

***

## How to use

### Basics

```python
from resf import *

initRes()                                   # Initializes new Table
addRes('Name', value)                       # Add a value to the table
addRes('Name', value, 'Unit', precision)    # Unit and Precision can be set
printRes()                                  # prints the resulting table
```

### Sample 1

```python
foo = 15
bar = 123 / 14

initRes()
addRes('Foo', foo, 'kg')
addEmpty()                                  # Add an empty line
addRes('0 digits of Bar', bar, precision=0)
addRes('4 digits of Bar', bar, precision=4)
printRes()
```

### Output 1

```
+-----------------+----------------+
| Name            | Value [Unit]   |
|-----------------+----------------|
| Foo             | 15.00 kg       |
|                 |                |
| 0 digits of Bar | 9              |
| 4 digits of Bar | 8.7857         |
+-----------------+----------------+
```
***

## All Functions

```python
initRes()
addRes(name, value, unit='', precision=2)
addEmpty()
printRes()
```

***
Uses [tabulate](https://pypi.org/project/tabulate/) to generate the table
