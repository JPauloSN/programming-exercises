def isPositive(num:float):
    if num > 0:
        return 0
    else:
        return 1

def isNulo(num:float):
    if num != 0:
        return 0
    else:
        return 1

def eqsg(a:float, b:float, c:float):
    return ((b**2)-((4 * a) * c)) 

delta = print(eqsg(1, 6, 3))
