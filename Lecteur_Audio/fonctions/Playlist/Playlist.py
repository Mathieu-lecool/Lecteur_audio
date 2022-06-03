from tkinter import *
from json import load, dump

info = load(open("config.vix", "r"))
background = info["background"]

def playliste():

    def AjouterPlaylite():
        try:
            Playlist = load(open("sauvegardes\playlistes.json", "r"))
            Playlist[Nom.get()] = []
            dump(Playlist, open("sauvegardes\playlistes.json", "w"))
            playliste_fenetre.destroy()
        except:
            pass

    playliste_fenetre = Tk()
    playliste_fenetre.config(background=background)
    playliste_fenetre.title("Playlist")
    playliste_fenetre.iconbitmap("Vixel.ico")

    frame = Frame(playliste_fenetre, bg=background)
    Label(frame, text="Nom de la playlist", bg=background).pack()
    Nom = Entry(frame)
    Nom.pack()
    frame.pack(pady=10)

    Button(playliste_fenetre, text="Créer", command=AjouterPlaylite, bg="orange").pack()

    playliste_fenetre.mainloop()