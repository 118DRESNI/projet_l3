from tkinter import *
window = Tk()

bgColor		= "#E6EAD8" 
textColor	= "#000000"

window.title("Application Test")
window.geometry("640x480")
window.minsize(640,480)
window.iconbitmap("window-icon.ico")
window.config(background= bgColor)

frame = Frame(window, bg=bgColor)

label_title = Label(label,text="bienvenue sur l'application", font=("Arial",20), bg=bgColor, fg=textColor)
label_title.pack()

frame.pack(expand=YES)

window.mainloop()
