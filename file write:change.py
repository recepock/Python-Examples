f = open('myfile.txt', 'a') 
f.write('data') 
f.write('compute') 
f.write('process') 
f.write('data\n') 
f.write('compute\n') 
f.write('process\n') 
f.close
f = open('myfile.txt', 'r')

print(f.readlines(5))

print(f.fileno())

f = open("newfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

print(f.isatty())
print(f.readable())
print(f.tell())

f = open("demofile2.txt", "a")
f.truncate(20)
f.close()


f = open("demofile2.txt", "r")
print(f.read())
f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])


places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile.txt', 'w') as filehandle:
    for listitem in places:
        filehandle.write('%s\n' % listitem)


