matris = [[2,3,4,5],[5,3,4,3],[6,4,0,-3]]
print(matris)
for satir in matris:
    for elaman in satir:
        print('{:4}'.format(elaman), end = '')
    print('\n')
    
print('.......\n')

matris2 = [[0]*4]*3
for satir in matris2:
    for elaman in satir:
        print('{:4}'.format(elaman), end = '')
    print('\n')
print('.......\n')
matris2[1][2]= '   r'
for satir in matris2:
    for elaman in satir:
        print('{:4}'.format(elaman), end = '')
    print('\n')


    
        