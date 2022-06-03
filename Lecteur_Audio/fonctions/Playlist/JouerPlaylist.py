from tkinter import *
from pygame import init
from pygame.mixer import Sound
from json import load
from time import sleep
from os.path import splitext

def PlayPlaylist():
    
    info = load(open("config.vix", "r"))
    background = info["background"]
    chemain = info["chemain"]

    init()

    Playlists = load(open("sauvegardes/playlistes.json", "r"))

    def Jouer():
        try:
            for musique in Playlists[Bar.get()]:
                son = Sound(f"{chemain}/{musique}")
                son.play()
                sleep(son.get_length() + 2)
        except:
            pass
    
    app = Tk()
    app.config(background=background)
    app.iconbitmap("Vixel.ico")

    Bar = Entry(app)
    Bar.grid(row=1, column=1)

    nb_colone = 1
    nb_row = 2
    for Playlist in Playlists:
        frame = Frame(app, bg="deepskyblue")
        Label(frame, text=Playlist, bg="deepskyblue").grid()
        for Musiques in Playlists[Playlist]:
            nom, extention = splitext(Musiques)
            Label(frame, text=nom, bg="deepskyblue").grid()
        frame.grid(row=nb_row, column=nb_colone, padx=10, pady=10)
        if nb_colone == 2:
            nb_colone = 1
            nb_row += 1
        else:
            nb_colone += 1

    Button(app, text="Jouer la Playlist", bg="orange", command=Jouer).grid(row=1, column=2, padx=10)
        
    app.mainloop()