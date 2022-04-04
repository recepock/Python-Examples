cevap = int(input('elektrik varsa 1 e basin'))
if cevap == 1:
    print('yardimi başka yerde arayın')
else:
    cevap = int(input('fişe takilysa 1 e basin'))
    if (cevap !=1):
        print('fişe takın')
    else:
        cevap = int(input('dügme aciksa 1 e basin'))
        if (cevap != 1):
            print('acma dugmesine basin')
        else:
            cevap = int(input('sigorta Ok se 1 e basin'))
            if (cevap !=1):
                print('sigortayi duzlet')
            else:
                 print('yardimi baska yerde arayin')
                
