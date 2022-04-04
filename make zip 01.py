global n

def gen(n):
    for i in range(n):
        yield i**2

list1 = [0,1,2,3, 4, 5]
list2 = ['a','b','c','d', 'e']
for t in zip(list1,list2):
    print(t)

print() 
  
for p in zip(list1,gen(6)):
    print(p)  
print() 
My_list = list(zip(range(10), range(10, 0, -1))) 

print(My_list)

tek_liste = list(zip(list1,list2))
print()
print(tek_liste)

