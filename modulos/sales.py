""" 
The module contains 3 functions:
1. Amount: return p*c
2. IGV: return amount * 0.18
3. Total : return amount + IGV
"""


def amount(p, c):
    return p * c


def igv(i):
    return i * 0.18


def total(i, igv_1):
    return i + igv_1
