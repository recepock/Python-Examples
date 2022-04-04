X = [[7,4,5],[6,17,8],[9,5,2]]
Y = [[9,8,6],[26,5,4],[13,6,11]]
sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        sonuc[i][j] = X[i][j] + Y[i][j]
        
for r in sonuc:
    print(r)

sonuc = X + Y
for r in sonuc:
    print(r)

