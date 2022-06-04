from json import dump, load
from datetime import date
from time import sleep
from tkinter import Tk, Scale, Button, Label
from pygame.mixer import Sound, init

info = load(open("config.vix", "r"))
background = info["background"]
chemain = info["chemain"]

def Play(MusiqueEnregistre, reload, Bar):

    lecture = True

    def Boucle():
        son.stop()
        while lecture:
            son.play()
            sleep(son.get_length()+2)

    def Stop():
        son.stop()
        lecture = False
        windows.destroy()
        return lecture

    try:
        MusiqueEnregistre[Bar.get() + ".mp3"]["utilisation"] = str(date.today())
        dump(MusiqueEnregistre, open("sauvegardes/musiques.json", "w"))
        init()
        son = Sound(chemain + Bar.get() + ".mp3")
        son.play()
        windows = Tk()
        windows.title(Bar.get())
        windows.config(background=background)
        windows.iconbitmap("Vixel.ico")
        windows.geometry("150x60")
        Button(windows, text="Lire en boucle", bg="orange", command=Boucle).pack(pady=2)
        Button(windows, text="Arreter", bg="lightcoral", command=Stop).pack(pady=2)
        windows.mainloop()
        reload()
    except: pass
