#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
from tkinter import *
from tkinter import messagebox as mb
import hashlib

class Adminlogin():

    def __init__(self, adminPWHash:str, id:str):
        self.accessGranted = False
        self.hash = adminPWHash
        self.id = id
        self.window = Tk()
        self.window.title('PeopleVoice - Connexion admin')
        typeIdLabel = Label(self.window, text='Veuillez entrer votre identifiant ci-dessous :')
        typeIdLabel.pack()
        self.idTextField = Entry(self.window, width=30)
        self.idTextField.pack()
        typePWLabel = Label(self.window, text="Veuillez entrer votre mot de passe ci-dessous :")
        typePWLabel.pack()
        self.pwTextField = Entry(self.window, width=30)
        self.pwTextField.pack()
        validateBtn = Button(self.window, text="Valider", command=self.validate)
        validateBtn.pack()
        self.window.mainloop()
        return None

    def validate(self):
        id = self.idTextField.get()
        password = self.pwTextField.get()
        bhashedUserEntry = hashlib.md5(password.encode())
        hashedUserEntry = bhashedUserEntry.hexdigest()
        if hashedUserEntry == self.hash and id == self.id:
            self.window.quit()
            self.accessGranted = True
        else:
            mb.showerror('Erreur d\'identification', 'Identifiant ou mot de passe incorrect.')
        return None

    def isAccessGranted(self) -> bool:
        return self.accessGranted
