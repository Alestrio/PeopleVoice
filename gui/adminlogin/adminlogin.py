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
        self.pwTextField = Entry(self.window, width=30)
        self.pwTextField.pack()
        validateBtn = Button(self.window, text="Valider", command=self.validate)
        validateBtn.pack()
        self.window.mainloop()
        return None

    def validate() -> bool:
        password = self.pwTextField.get()
        bhashedUserEntry = hashlib.md5(password.encode())
        hashedUserEntry = bhashedUserEntry.hexdigest()
        if hashedUserEntry == self.hash:
            self.window.quit()
            return True #Retour non utilisé pour l'instant
        else:
            return False
