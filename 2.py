import math



def add(c1, c2):
    re = c1[0] + c2[0]
    im = c1[1] + c2[1]
    resp = re, im
    return resp

def multi(c1, c2):
    re = c1[0]*c2[0] - c1[1]*c2[1]
    im = c1[0]*c2[1] + c1[1]*c2[0]
    resp = re, im
    return resp

def sub(c1, c2):
    re = c1[0] - c2[0]
    im = c1[1] - c2[1]
    resp = re, im
    return resp

def div(c1, c2):
    if c2[0] != 0 or c2[1] != 0:
        re = round(((c1[0]*c2[0])+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        im = round(((c2[0]*c1[1])-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2), 3)
        resp = re, im
        return resp

    else:
        raise ValueError('Can not divide by zero')


def mod(c1):
    m = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
    return m

def conj(c1):
    re = c1[0]
    im = c1[1]*-1
    resp = re, im
    return resp


def polar(c1):
    if c1[0] < 0 and c1[1] < 0:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round(2*math.pi-(-1*(math.atan2(c1[1], c1[0]))), 2)
        resp = p, o
        return resp
    elif c1[0] > 0 > c1[1]:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round((2*math.pi + math.atan2(c1[1], c1[0])), 2)
        resp = p, o
        return resp
    else:
        p = round(math.sqrt(c1[0] ** 2 + c1[1] ** 2), 2)
        o = round((math.atan2(c1[1], c1[0])), 2)
        resp = p, o
        return resp

def cart(c1):
    re = round(c1[0]*math.cos(c1[1]))
    im = round(c1[0]*math.sin(c1[1]))
    resp = re, im
    return resp


def phase(c1):
    if c1[0] < 0 and c1[1] < 0:
        ph = round(2 * math.pi - (-1 * (math.atan2(c1[1], c1[0]))), 2)
        return ph
    elif c1[0] > 0 > c1[1]:
        ph = round((2 * math.pi + math.atan2(c1[1], c1[0])), 2)
        return ph
    else:
        ph = round((math.atan2(c1[1], c1[0])), 2)
        return ph
