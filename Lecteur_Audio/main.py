import pickle
from pygame import init
from pygame.mixer import Sound
from json import dump, load
from subprocess import run
from datetime import date
from os import listdir
from os.path import splitext
from tkinter import Tk, Label, Entry, Button, Frame
from fonctions import Compte, Parametres, LireMusiques
from fonctions.Playlist import Playlist, AjPlayliste, JouerPlaylist

info = load(open("config.vix", "r"))
background = info["background"]
chemain = info["chemain"]

try: user = pickle.load(open("compte.bin", "rb"))
except: user = "none none none"

musiquePath = chemain
MusiqueEnregistre = load(open("sauvegardes/musiques.json", "r"))
listeMusiques = listdir(musiquePath)

for mp3 in listeMusiques:
    if splitext(mp3)[1] != ".mp3": listeMusiques.remove(mp3)

def reload():
    app.destroy()
    run(f"python {__file__}", shell=True)

def SupprPlaylist():
    try:
        playliste = MusiqueEnregistre[Bar.get() + ".mp3"]["playliste"]
        MusiqueEnregistre[Bar.get() + ".mp3"]["playliste"] = "Aucune"
        dump(MusiqueEnregistre, open("sauvegardes/musiques.json", "w"))
        playlist = load(open("sauvegardes/playlistes.json", "r"))
        playlist[playliste].remove(Bar.get()+".mp3")
        dump(playlist, open("sauvegardes/playlistes.json", "w"))
        reload()
    except: pass

def Favoris():
    MusiqueEnregistre[Bar.get() + ".mp3"]["favoris"] = not MusiqueEnregistre[Bar.get() + ".mp3"]["favoris"]
    dump(MusiqueEnregistre, open("sauvegardes/musiques.json", "w"))
    reload()

app = Tk()
app.title("Lecteur Audio")
app.config(background=background)
app.iconbitmap("Vixel.ico")
app.resizable(0, 1)

Button(app, text="Créer une playlist", command=Playlist.playliste, bg="lightcoral").grid(row=1, padx=5)
Button(app, text="Parametres", command=lambda: Parametres.parametre(reload), bg="dodgerblue").grid(row=2)

if user != "none none none": Label(app, text=f"Connecté avec :\n{user.split(' ')[0]}", bg="dodgerblue").grid(row=3)
else: Button(app, text="Se connecter", bg="dodgerblue", command=lambda: Compte.compte(reload)).grid(row=3)

Bar = Entry(app)
Bar.grid(column=3, row=1)

Button(app, text="Play", command=lambda: LireMusiques.Play(MusiqueEnregistre, reload, Bar), bg="orange").grid(column=4, row=1)
Button(app, text="Ajouter / Supprimer\ndes favoris", command=Favoris, bg="gold").grid(column=3, row=2)
Button(app, text="Supprimer des playlists", command=SupprPlaylist, bg="lightcoral").grid(column=3, row=3)
Button(app, text="Ajouter à une playlist", command=lambda: AjPlayliste.fonction(reload, Bar.get()), bg="cyan").grid(column=4, row=2)
Button(app, text="Jouer une playlist", command=JouerPlaylist.PlayPlaylist, bg="violet").grid(column=4, row=3)

compteur_rangée = 0
compteur_collone = 1
row = 0
nb_frame = 0
nb_pixel = 0

for musique in listeMusiques:
    if (compteur_collone % 2) == 0: position = 2
    else: position = 1
    if (compteur_rangée % 2) == 0: row += 1
    if not musique in MusiqueEnregistre:
        MusiqueEnregistre[musique] = {}
        MusiqueEnregistre[musique]["utilisation"] = str(date.today())
        MusiqueEnregistre[musique]["favoris"] = False
        MusiqueEnregistre[musique]["playliste"] = "Aucune"
        dump(MusiqueEnregistre, open("sauvegardes/musiques.json", "w"))
    if MusiqueEnregistre[musique]["favoris"] == True: couleur = "gold"
    else: couleur = "deepskyblue"
        

    frame = Frame(app)
    Label(frame, bg=couleur, text=f"Nom: {splitext(musique)[0]}\nDernière utilistation: {MusiqueEnregistre[musique]['utilisation']}\nPlaylist: {MusiqueEnregistre[musique]['playliste']}").grid()
    frame.grid(row=row, column=position, padx=10, pady=10)
    compteur_collone += 1
    compteur_rangée += 1
    nb_frame += 1
    if not (nb_frame % 2) == 0: nb_pixel += 75

app.geometry(f"1010x{nb_pixel}")

app.mainloop()