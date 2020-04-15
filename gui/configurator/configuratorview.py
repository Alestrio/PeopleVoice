#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import *
from tkinter import messagebox as mb

class Configuratorview:

    def __init__(self, controller):
        self.hasSucceeded = False
        self.controller = controller
        return None

    def createAndShowWindow(self):
        self.window = Tk()
        self.window.title('PeopleVoice - Premier démarrage')

        idLabel = Label(self.window, text='Veuillez définir un identifiant :')
        self.idTF = Entry(self.window)
        pwlabel = Label(self.window, text='Veuillez définir le mot de passe :')
        self.pwTF = Entry(self.window)
        confPWLabel = Label(self.window, text='Veuillez confirmer votre mot de passe :')
        self.confPWTF = Entry(self.window)
        validateBtn = Button(self.window, text='Valider', command=self.validate)

        idLabel.pack()
        self.idTF.pack()
        pwlabel.pack()
        self.pwTF.pack()
        confPWLabel.pack()
        self.confPWTF.pack()
        validateBtn.pack()

        self.window.mainloop()
        return None

    def validate(self):
        if self.sanityCheck():
            if self.controller.validate(self.idTF.get(), self.pwTF.get(), self.confPWTF.get()):
                self.hasSucceeded = True
                self.window.quit()
            else:
                mb.showerror(title='PeopleVoice - Premier démarrage', message='Les mots de passe ne correspondent pas.')
        else:
            mb.showerror('PeopleVoice - Premier démarrage', 'Entrée invalide')
        return None

    def sanityCheck(self) -> bool:
        if self.idTF.get() != '' and self.pwTF.get() != '' and self.confPWTF.get() != '':
            return True
        else:
            return False
