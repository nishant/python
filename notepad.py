from tkinter import *
from tkinter.filedialog import *
 
filename = None
WINDOW_SIZE = 500

def new_file():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)

def save_file():
    try:
        global filename
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        save_as_file()

def save_as_file():
    f = asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        import tkinter.messagebox
        tkinter.messagebox.showerror(title = 'Error!', message = "Unable to save file.")

def open_file():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title('Notepy')
root.minsize(width = WINDOW_SIZE, height = WINDOW_SIZE)
root.maxsize(width = WINDOW_SIZE, height = WINDOW_SIZE)
text = Text(root, width = WINDOW_SIZE, height = WINDOW_SIZE)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = new_file)
filemenu.add_command(label = 'Open', command = open_file)
filemenu.add_command(label = 'Save', command = save_file)
filemenu.add_command(label = 'Save As', command = save_as_file)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)

root.config(menu = menubar)
root.mainloop()
