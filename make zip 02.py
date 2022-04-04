list1 = [1,2,3,4,5,]
list2 = [5,6,7,8,9]

for (x,y) in zip(list1,list2):
    print(x+y)

toplamlar_listesi = [x+y for (x,y) in zip(list1,list2) ]

print(toplamlar_listesi)