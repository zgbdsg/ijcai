__author__ = 'zgb'

def gen(value,type):
    len = 0
    re = []
    if type == 1:
        len = 8

    if type == 2:
        len = b

    if type == 3:
        len = c

    loc = int(value[1:])

    for i in range(len):
        if i == loc-1:
            re.append(1)
        else:
            re.append(0)

    return re