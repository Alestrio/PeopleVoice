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

    def validatePw(self, password:str):
        model.getVoterRow(password)
        return None

    def selectAsChoiceOne(self, voterChoice, candidateChoice):
        if voterSelection != None and candidateSelection != None:
            mb.showerror(title='Erreur de selection', message='Vous ne devez avoir qu\'une sélection pour valider')
        elif voterSelection != None and candidateSelection == None:
            self.model.setChoiceOne(voterSelection)
        elif candidateSelection != None and voterSelection == None:
            self.model.setChoiceOne(candidateSelection)
        else:
            mb.showerror(title='Erreur', message='Erreur inconnue')

    def selectAsChoiceTwo(self, voterChoice, candidateChoice):
        if voterSelection != None and candidateSelection != None:
            mb.showerror(title='Erreur de selection', message='Vous ne devez avoir qu\'une sélection pour valider')
        elif voterSelection != None and candidateSelection == None:
            self.model.setChoiceTwo(voterSelection)
        elif candidateSelection != None and voterSelection == None:
            self.model.setChoiceTwo(candidateSelection)
        else:
            mb.showerror(title='Erreur', message='Erreur inconnue')

    def onSessionOk(self):
        login = adminlogin.Adminlogin()
        if login.isAccessGranted():
            self.model.endSession()
        return None
