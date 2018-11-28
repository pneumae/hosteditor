import platform
from shutil import copy
#from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename

#print(platform.system())

root = Tk()
root.withdraw()
filename = askopenfilename()
root.destroy()
#print(filename)

copy(filename,'./temphost')

#f = open(filename, 'r')
#message = f.read()
#print(message)
#f.close()

ip = ""
hostname = ""

f = open('./temphost', 'a')
#message = f.read()
#print(message)


widgettext = ""

def drawInputWindow(inputField):

    def printtext():
        global e
        global widgettext
        string = e.get()
        widgettext = string
        root.destroy()

    root = Tk()

    root.title('Name')

    t = Label(root, text=inputField)
    t.pack()

    global e
    e = Entry(root)
    e.pack()
    e.focus_set()

    b = Button(root,text='Submit',command=printtext)
    b.pack(side='bottom')
#root.destroy()
    root.mainloop()

drawInputWindow("IP")
ip = widgettext
drawInputWindow("Hostname")
hostname = widgettext

f.write('\n' + ip + '\t' + hostname)

f.close()
