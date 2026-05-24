import time
a=0
b=0
last = time.perf_counter()
while True:
    this = time.perf_counter()
    a += this-last
    if a >=1:
        a -= 1
        b += 1
        print(b)
    last = this