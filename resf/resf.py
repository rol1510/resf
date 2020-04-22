from tabulate import tabulate

class Result:
    def __init__(self, name, value, unit, precision):
        self.name = name
        self.value = value
        self.unit = unit
        self.precision = precision

_resultBuffer = []

def initRes():
    global _resultBuffer
    _resultBuffer = []

def addRes(name, value, unit='', precision=2):
    global _resultBuffer
    _resultBuffer.append(Result(name, value, unit, precision))

def addEmpty():
    addRes('', None)
    pass

def printRes():
    global _resultBuffer
    table = [] # name, value + unit
    for res in _resultBuffer:
        if res.value is None:
            table.append(['', ''])
        else:
            val = '{0:9.{1}f}'.format(res.value, res.precision)
            table.append([
                res.name,
                f'{val} {res.unit}'
            ])
    print(tabulate(table, headers=['Name', 'Value [Unit]'], tablefmt='psql', stralign='left'))

