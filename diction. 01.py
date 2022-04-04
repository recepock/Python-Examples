d = {}  

print(d)
print()


d['recep']= 21
print(d)
print()
d['genel']= 'sistemler'
print(d)
print()

d['ogle yemegi']= 'lunch'
print(d)
print()

print(d['ogle yemegi'])
print()

kelime = 'ogle yemegi'
if kelime in d:
    print(d[kelime])
else:
    print(kelime + ' bulunamadı')
    
