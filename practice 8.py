def topla(*sayilar):
    print(sayilar)
    s = 0
    for i in sayilar:
        s +=i
    return s

print(topla(3,4))
print(topla(3,4,8))
print(topla(3,4,6,7,8,8,0,-1,5,-9))
        