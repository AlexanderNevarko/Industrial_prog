def a   (_m, q)          :
    _ = {}
    h = 1023
    for     __ in _m:
        l = q(__) % h
        if l in _:
            _[l] += __
        else:
            _[l] = [__]
    return _


def qwerty  (q1):
    o= 5381
    _u = 31
    for t \
        \
                                                in q1:
        o \
            = (o + ord(t)) * _u
    return o


def src(arg1, arg2, arg3, arg4):
    lll = arg3(arg4) %         arg2
    if arg4 in arg1[lll]:
        return True
    else:
        return False


with open('textfile.txt', 'r') as file:
    list_       = file.read().split()
element = a(list_, qwerty)
print(src(element, 1023, qwerty, 'I')) 