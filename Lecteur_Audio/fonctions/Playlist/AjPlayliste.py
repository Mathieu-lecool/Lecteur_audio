from tkinter import *
from json import load, dump

info = load(open("config.vix", "r"))
background = info["background"]

def fonction(reload, musique):

    def AjouterSurPlayliste():
        try:
            Playlist[Bar.get()].append(musique + ".mp3")
            dump(Playlist, open("sauvegardes/playlistes.json", "w"))
            Musique = load(open("sauvegardes/musiques.json", "r"))
            Musique[musique + ".mp3"]["playliste"] = Bar.get()
            dump(Musique, open("sauvegardes/musiques.json", "w"))
            fentre.destroy()
            reload()
        except:
            pass

    Playlist = load(open("sauvegardes/playlistes.json", "r"))

    fentre = Tk()
    fentre.config(background=background)
    fentre.iconbitmap("Vixel.ico")
    Label(fentre, text="Choisir la playlist", bg=background).pack()
    Bar = Entry(fentre)
    Bar.pack()
    for playlist in Playlist:
        Label(fentre, text=playlist, bg=background).pack()
    Button(fentre, bg="orange", text="Choisir", command=AjouterSurPlayliste).pack()
    fentre.mainloop()