# resf - Result Formatter

A simple package for displaying calculation results in a textbased table

## Sample
'''
initRes()                                   # Initializes new Table
addRes('name', value, 'Unit', precision)    # To add a value to the table
addRes('name', value)                       # unit and precision are not required
printRes()                                  # prints the resulting table
'''

*Uses tabulate to generate the table (https://pypi.org/project/tabulate/)