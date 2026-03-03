def add(*b, **c):
    hap = 0
    for val in b:
        hap += val
    for val in c:
        hap += c[val]
    return hap


print(add(10, 20, 30, mbc=40, kbs=40))
print(add(10, 20, 30, 40, one=50, two=60, three=70))