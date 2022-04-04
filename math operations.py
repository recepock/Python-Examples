sayilar = []
for i in range (10,3000000):
    tot = 0
    jindex = 1
    stri = str(i)
    for j in stri:
        tot = tot + pow(int(j),jindex)
        jindex = jindex + 1
        if tot == i:
            sayilar.append(i)
            print(i)
                
print(sayilar)
