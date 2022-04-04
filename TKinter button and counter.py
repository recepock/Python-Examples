from tkinter import Tk,Button

count = 0

def guncelle():
    global b,count
    count +=1
    b.configure(background= 'green', text = 'Click Count =' + str(count) )
    print('updating')
    b.pack()


root = Tk()
b = Button(root)
b.configure(background= 'blue', text = 'Click Count = 0',command = guncelle)
b.pack()
root.mainloop()