import math

def radius(num):
    area= math.pi * (num**2)
    curcumference=2*math.pi*num
    return area , curcumference

Area , Curcumference = radius(3)

print(round(Area, 2) , round(Curcumference , 2))