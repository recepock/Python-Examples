t = (2,'abc',23.67)
print(t)

sayi,yazi,kesirli = t

print(sayi*kesirli)
print(yazi)

_,yazi, kesirli = t

t = list(t)
print(t)
t[0]= 22
print(t)
t = tuple(t)
print(t)


