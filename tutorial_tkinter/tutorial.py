import tkinter as tk
"""
try:
    from ctypes import windll
finally:
"""
fntr = tk.Tk()
fntr.title('tutoriel Tkinter')
#dimensions de la fenetre
fntr_w = 720
fntr_h = 480

#obtenir les dimensions d'ecran
scrn_w = fntr.winfo_screenwidth()
scrn_h = fntr.winfo_screenheight()

#trouver le centre de l'ecran
ctr_x = int(scrn_w/2 -  fntr_w/2)
ctr_y = int(scrn_h/2 -  fntr_h/2)

#definir la geometrie de la fentre
fntr.geometry(f'{fntr_w}x{fntr_h}+{ctr_x}+{ctr_y}')
fntr.resizable(False, False)
fntr.attributes('-alpha',0.5)

msg_bienvenue = tk.Label(fntr, text="Bonjour, Monde!")
msg_bienvenue.pack()


fntr.mainloop()