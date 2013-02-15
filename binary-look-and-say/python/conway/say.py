class Sayer():
    def __init__(self):
        pass

    def say(self, origin):
        result = ''
        for block in blocks(origin):
            result += str(len(block)) + block[0];
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
    
