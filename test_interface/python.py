from tkinter import *

# fonction d'incrementation du label sous titre
def addOne():
    ctr = int(label_subtitle["text"])
    label_subtitle["text"] = f"{ctr + 1}"

# valeur hex des couleurs de fond et de texte
bgColor		= "#E6EAD8" 
textColor	= "#000000"


# creation d'une nouvelle fenetre et parametrage resolution
window = Tk()
window.title("Application Test")
window.geometry("720x480")
window.minsize(720,480)
window.maxsize(720,480)
#window.iconbitmap("window-icon.ico")
window.config(background= bgColor)

# frame globale du dessus
frame_top = Frame(
    master=window,
    bg=bgColor, 
    bd=1,
    relief=SUNKEN,
    padx=5,pady=5
    )
frame_top.pack(fill=X)

# frame globale du dessous
frame_bot = Frame(
    master=window,
    bg=bgColor, 
    bd=1,
    relief=SUNKEN,
    padx=5,pady=5
    )
frame_bot.pack(fill=X)

# frame de gauche dans la frame top
frame = Frame(
    master=frame_top,
    bg=bgColor, 
    bd=1,
    relief=SUNKEN,
    padx=5,pady=5
    )
frame.pack(side=LEFT, fill=Y, padx=5,pady=5)

# frame de droite dans la frame top
frame_droite = Frame(
    master=frame_top,
    bg=bgColor, 
    bd=1,
    relief=SUNKEN,
    padx=5,pady=5
    )
frame_droite.pack(side=RIGHT, fill=Y, padx=5,pady=5)

# ajouter un titre
label_title = Label(
    master=frame,
    text="bienvenue sur l'application",
    font=("Arial",20),
    bg=bgColor,
    fg=textColor)
label_title.pack()

# ajouter un titre
label_title = Label(
    master=frame_droite,
    text="bienvenue",
    font=("Arial",20),
    bg=bgColor,
    fg=textColor)
label_title.pack()

# ajouter un SOUS titre
label_subtitle = Label(
    master=frame,
    text="0",
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
    fg=textColor,
    command=addOne)
bouton.pack()

# ajouter un bouton
bouton_bot = Button(
    master=frame_bot,
    text="cliquez",
    font=("Arial",10),
    bg=bgColor,
    fg=textColor,
    command=addOne)
bouton.pack()

# afficher le frame et son contenu

window.mainloop()
