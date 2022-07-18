import numpy as np
from decimal import Decimal


def lin_equ(l1, l2):
    """Line encoded as l=(x,y)."""
    m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
    c = (l2[1] - (float(m) * l2[0]))
    return m, c
    

if __name__ == '__main__':
    m1,c1 = lin_equ((0,525.5), (190.46, 815.5))
    m2,c2 = lin_equ((0,664.5), (111.04, 1072.5))
    m1,c1 = lin_equ((0,700), (128.58, 1019))

    print(m2)



