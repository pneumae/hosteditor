import platform
from shutil import copy
from tkinter import *
from tkinter.filedialog import askopenfilename
from os import remove

osdict = {
"Linux" : "/etc/hosts",
"Darwin" : "/etc/hosts",
"Windows" : "C:\Windows\System32\drivers\etc\hosts"
}
filename = ""

def fileBrowser():
    global filename
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    root.destroy()
#print(filename)

def choosePathEntryMethod():
    def buttonPress(option):
        global entrychoice
        if(option == 0):
            entrychoice = "default"
            root.destroy()
        if(option == 1):
            entrychoice = "browse"
            root.destroy()

    root = Tk()
    root.title("Host editor")

    l = Label(root, text="Use default path or custom location")
    l.pack()

    b1 = Button(root, text="Default", command=lambda: buttonPress(0))
    b1.pack(side=LEFT)

    b2 = Button(root, text="Browser", command=lambda: buttonPress(1))
    b2.pack(side=RIGHT)

    root.mainloop()

choosePathEntryMethod()

if(entrychoice == "default"):
    operatingsystem = platform.system()
    filename = osdict[operatingsystem]
if(entrychoice == "browse"):
    fileBrowser()

copy(filename,'./temphost')

ip = ""
hostname = ""

f = open('./temphost', 'a')

widgettext = ""

def drawInputWindow(inputField):
    global ip
    global hostname

    def printtext():
        global e
        global widgettext
        string = e.get()
        widgettext = string
        root.destroy()

    root = Tk()

    root.title("Host editor")

    t = Label(root, text=inputField)
    t.pack()

    global e
    e = Entry(root)
    e.pack()
    if(inputField=="IP"):
        e.insert(0,ip)
    if(inputField=="Hostname"):
        e.insert(0,hostname)
    e.focus_set()

    b = Button(root,text='Submit',command=printtext)
    b.pack(side='bottom')
#root.destroy()
    root.mainloop()

def askForUserInput():
    global ip
    global hostname
    drawInputWindow("IP")
    ip = widgettext
    drawInputWindow("Hostname")
    hostname = widgettext
    userEntryConfirmation()


def userEntryConfirmation():
    global ip
    global hostname

    def confirmButton():
        root2.destroy()
    def cancelButton():
        root2.destroy()
        askForUserInput()
    root2 = Tk()
    root2.title('Host editor')
    l1 = Label(root2, text="Confirm entry")
    l1.pack()
    confirmmessage = "IP: " + ip + " Hostname: " + hostname
    Label(root2, text=confirmmessage).pack()
    Button(root2, text="Ok", command=confirmButton).pack(side=LEFT)
    Button(root2, text="Cancel", command=cancelButton).pack(side=RIGHT)
    root2.mainloop()

askForUserInput()

f.write('\n' + ip + '\t' + hostname)
f.close()

try:
    copy('./temphost',filename)
    remove('./temphost')
except Exception:
    root = Tk()
    def confirmButton():
        root.destroy()
    root.title("Host editor")
    Label(root, text="No admin privileges").pack()
    Button(root, text="Ok", command=confirmButton).pack()
    root.mainloop()
    remove('./temphost')
