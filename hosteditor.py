import platform
from shutil import copyfile
#from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename

print(platform.system())

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)

copyfile(filename,'./test')

#f = open(filename, 'r')
#message = f.read()
#print(message)
#f.close()


#f = open('./test', 'r')
ip = "127.0.0.1"
hostname = "home"

f = open('./test', 'a')
#message = f.read()
#print(message)
f.write('\n' + ip + '\t' + hostname)

f.close()

def printtext():
        global e
        string = e.get()
        print(string)


root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()
