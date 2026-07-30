import math


def scientific_notation(a):
    if a < 10000:
        output = a
    else:
        output = f"{int(a//10**(math.floor(math.log10(a))))}.{int(a//10**(math.floor(math.log10(a))-2))-100*int(a//10**(math.floor(math.log10(a))))}e{math.floor(math.log10(a))}"
    return output
print(scientific_notation(int(input(""))))