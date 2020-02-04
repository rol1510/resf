# resf - Result Formatter

A simple package for displaying calculation results in a textbased table
***
## How to use
Basics
```python
from resf import *

initRes()                                   # Initializes new Table
addRes('Name', value, 'Unit', precision)    # add a value to the table
addRes('Name', value)                       # unit and precision are not required
printRes()                                  # prints the resulting table
```
Sample 1
```python
foo = 15
bar = 123 / 13

initRes()
addRes('Foo', foo, 'V')
addRes('5 digits of Bar', bar, precision=5)
printRes()
```
Output 1
```
 +-----------------+----------------+
 | Name            | Value [Unit]   |
 |-----------------+----------------|
 | Foo             | 15.00 V        |
 | 5 digits of Bar | 9.46154        |
 +-----------------+----------------+
```
***
Uses [tabulate](https://pypi.org/project/tabulate/) to generate the table
