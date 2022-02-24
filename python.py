from tkinter import *


# valeur hex des couleurs de fond et de texte
bgColor		= "#E6EAD8" 
textColor	= "#000000"


# creation d'une nouvelle fenetre et parametrage resolution
window = Tk()
window.title("Application Test")
window.geometry("640x360")
window.minsize(640,360)
window.maxsize(640,360)
#window.iconbitmap("window-icon.ico")
window.config(background= bgColor)

# declarer la frame et sa couleur de fond 
frame = Frame(
    master=window,
    bg=bgColor, 
    bd=1,
    relief=SUNKEN,
    padx=5,pady=5
    
    )

# ajouter un titre
label_title = Label(
    master=frame,
    text="bienvenue sur l'application",
    font=("Arial",20),
    bg=bgColor,
    fg=textColor)
label_title.pack()

# ajouter un SOUS titre
label_subtitle = Label(
    master=frame,
    text="voici un sous titre",
    font=("Arial",10),
    bg=bgColor,
    fg=textColor)
label_subtitle.pack()

# ajouter un bouton
bouton = Button(
    master=frame,
    text="cliquez",
    font=("Arial",10),
    bg=bgColor,
    fg=textColor)
bouton.pack()

# afficher le frame et son contenu
frame.pack(side=LEFT, fill=Y, padx=5,pady=5)

window.mainloop()
