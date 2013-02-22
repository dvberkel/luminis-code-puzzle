class Sayer():
    def __init__(self, base = 10):
        self._base = base

    def say(self, origin):
        result = ''
        for block in blocks(origin):
            result += convert(len(block), self._base) + block[0];
        return result

def blocks(origin):
    result, start = [], 0
    while (start < len(origin)):
        end = findBreak(origin, start)
        result.append(origin[start:end])
        start = end
    return result

def findBreak(origin, start = 0):
    index = start
    while (index < len(origin) and origin[start] == origin[index]):
        index += 1;
    return index;
    
def convert(number, base):
    result = ''
    while (number > 0):
        modulus = number % base;
        number /= base
        result = str(modulus) + result
    return result
