#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import tkinter as tk
import hashlib

class Adminlogin():

    def __init__(self, adminPWHash:str):
        self.hash = adminPWHash
        self.window = Tk()
        typePWLabel = Label(self.window, text="Veuillez entrer votre mot de passe ci-dessous:")*
        typePWLabel.pack()
        self.pw = StringVar()
        pwTextField = Entry(self.window, textvariable=self.pw, width=30)
        pwTextField.pack()
        validateBtn = Button(self.window, text="Valider", command=self.validate)
        validateBtn.pack()
        self.window.mainloop()
        return None

    def validate() -> bool:
        password = self.pw
        bhashedUserEntry = hashlib.md5(encode(password))
        hashedUserEntry = bhashedUserEntry.hexdigest()
        if hashedUserEntry == self.hash:
            self.window.quit()
            return True #Retour non utilisé pour l'instant
        else:
            return False
