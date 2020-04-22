from resf import *
# initRes()
# addRes('daf', 15, 'N')
# addEmpty()
# addRes('daf 2', 15.3334, 'N', 5)
# printRes()

foo = 15
bar = 123 / 14

initRes()
addRes('Foo', foo, 'kg')
addEmpty()                                  # Add an empty line
addRes('0 digits of Bar', bar, precision=0)
addRes('4 digits of Bar', bar, precision=4)
printRes()