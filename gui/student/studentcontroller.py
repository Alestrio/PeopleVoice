#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the controller. There, we will gather the events from the view, and apply
# the actions related to those events. That class also gather and send data to and from
# the model, who does the computation and the link with the rest of the software.
#
from tkinter import messagebox as mb
import sys
sys.path.insert(0, "../adminlogin")
import adminlogin

class Studentcontroller:

    def __init__(self, model):
        self.model = model
        return None

    def setView(self):
        self.view = self.model.view
        return None

    def onSessionOk(self):
        login = adminlogin.Adminlogin()
        if login.isAccessGranted():
            self.model.endSession()
        return None

    def showMbSecondTurn(self):
        mb.showinfo(title='Tour suivant', message='Le système passe au second tour')
        return None

    def showMbNoChoice(self):
        mb.showerror(title='Erreur', message='Vous devez selectionnner une personne')

    def choiceOk(self):
        self.model.clearCurrentVoter()
        self.view.clearVoterInfos()
        self.view.clearChoicesInfos()
        return None
