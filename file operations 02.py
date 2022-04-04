f = open('denemeDosya.txt', 'a')
f.write('Akşam ne yapıyorsun?')
print(f.readable())
print(f.writable())

f.close()


f = open('denemeDosya.txt', 'r')
print(f.read())
f.flush()
print(f.fileno())
print(f.readable())
print(f.writable())
print(f.readlines(2))
f.close()




