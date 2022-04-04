a = [[7,4,5],[6,17,8],[9,5,2]]
b = [[9,8,6],[26,5,4],[13,6,11]]
c =[[0,0,0],[0,0,0],[0,0,0]]
print('c matrisi:\n')
N = 3
M = 3
for i in range(M):
    for j in range(N):
        toplam = 0.0
        for k in range(N):
            toplam +=a[i][k]*b[k][j]
        c[i][j]= toplam
        print('{:4}'.format(c[i][j]), end = ' ')
    print() 
 
