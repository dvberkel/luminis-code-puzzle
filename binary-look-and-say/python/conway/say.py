class Sayer():
    def __init__(self, base = 10):
        self._base = base

    def say(self, origin):
        result = ''
        for block in blocks(origin):
            result += convert(len(block), self._base) + block[0];
        return result

def blocks(origin):
    if (len(origin) == 0):
        return []
    else:
        index = findBreak(origin);
        return [ origin[0:index] ] + blocks(origin[index:])

def findBreak(origin):
    index = 0
    while (index < len(origin) and origin[0] == origin[index]):
        index += 1;
    return index;
    
def convert(number, base):
    result = ''
    while (number > 0):
        modulus = number % base;
        number /= base
        result = str(modulus) + result
    return result
