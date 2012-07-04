from Tkinter import *
import os

def exit(event):
    #Exit and shutdown our app
    os.system('C:\Progs\shutdown.bat')
    root.destroy()

def autostart():
    #run this app after timeout
    os.system('C:\Progs\DAMJukeBox\DAMJukeBox.exe')

def key(event):
    if event.char == 'a':
        #DAM JukeBox
        root.after_cancel(autosched) # kill autostart
        os.system('C:\Progs\DAMJukeBox\DAMJukeBox.exe')
    elif event.char == 'd':
        #Itunes
        root.after_cancel(autosched) # kill autostart
        os.system('C:\Progs\itunes.lnk')        
    elif event.char == '1':
        #Mame/Mala
        root.after_cancel(autosched) # kill autostart
        os.system('C:\Progs\Mala.bat')
    elif event.char == 'q':
        #Quit
        root.destroy()

root = Tk()

# make it cover the entire screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.config(bg='black')

root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", exit)
root.bind('<Key>', key)

photo = PhotoImage(file="background.gif")
w = Label(root, image=photo, cursor="plus")
w.photo = photo
w.config(bg='black')
w.pack()

#schedule our default app to start after 10 seconds
autosched = root.after(10000, autostart)
root.mainloop()
