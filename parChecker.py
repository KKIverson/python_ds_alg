from pythonds.basic.stack import Stack


def parChecker(parstring):
    s = Stack()
    match = True
    pos = 0
    while pos < len(parstring) and match:
        par = parstring[pos]
        if par in '([{<':
            s.push(par)
        else:
            if s.isEmpty():
                match = False
                break
            top = s.pop()
            match = parMatch(top, par)
        pos += 1
    if not s.isEmpty():
        match = False
    return match


def parMatch(top, par):
    right = ')]}>'
    left = '([{<'
    return left.index(top) == right.index(par)


print(parChecker('([<>]>'))
