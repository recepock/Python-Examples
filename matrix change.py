n = 4
r = 5
c = 5
matris = [[n]*c]*r

for satir in matris:
    for elaman in satir:
        print('{:4}'.format(elaman), end = '')
    print('\n')  

n = n *2
 
for i in range(r):
    for j in range (c):
        matris[i][j]= n
    print('\n')


for satir in matris:
    for elaman in satir:
        print('{:4}'.format(elaman), end = '')
    print('\n')