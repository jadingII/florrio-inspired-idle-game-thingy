from math import log10, floor

def scientific(num):
    mantissa = 0
    exponent = 0
    if num >= 10000:
        mantissa = int(num//floor(log10(num)))
    else:
        return str(num)
print(scientific(int(input("number: "))))