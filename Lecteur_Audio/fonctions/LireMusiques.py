from json import dump, load
from threading import Thread
from time import sleep
from datetime import date
from tkinter import Tk, Scale, Button, Label
from pygame.mixer import Sound, init

info = load(open("config.vix", "r"))
background = info["background"]
chemain = info["chemain"]

def Play(MusiqueEnregistre, reload, Bar):

    lecture = True

    def Boucle():
        while lecture:
            son.play()
            sleep(son.get_length())

    def get_volume():
        volume = 1.0
        while lecture:
            MusiqueVolume = Volume.get()
            son.set_volume(MusiqueVolume)
            if MusiqueVolume != volume:
                LabelVolume["text"] = f"Volume : {son.get_volume()}"
                windows.update()

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
        reload()
        windows = Tk()
        windows.title(Bar.get())
        windows.config(background=background)
        windows.iconbitmap("Vixel.ico")
        LabelVolume = Label(windows, text=f"Volume : {son.get_volume()}")
        LabelVolume.grid(row=1, column=1, padx=5, pady=3)
        Volume = Scale(windows, from_=0.2, to=1.0)
        Volume.grid(row=2, column=1, padx=5)
        Button(windows, text="Lire en boucle", bg="orange", command=Stop).grid(row=1, column=2)
        Button(windows, text="Arreter", bg="lightcoral", command=Stop).grid(row=2, column=2)
        windows.mainloop()
    except: pass