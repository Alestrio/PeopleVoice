#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the controller. There, we will gather the events from the view, and apply
# the actions related to those events. That class also gather and send data to
# the model, who does the computation, updates the view, and does
# the link with the rest of the software.
#
import admin
import adminview
from tkinter import *
import random
import string
import hashlib
from tkinter import messagebox as mb

class Admincontroller():

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.passwords = list()
        return None


    def validateAddVoter(self):
        fullname = self.view.getNewVoterFullname()
        #password generation:
        password = ''
        for i in range(0,9):
            password += random.choice(string.ascii_letters)
        #Saving that password to display them all at the end of the config
        self.passwords.append(fullname[1] + " " + fullname[0] + " " + '::' + " " + password)
        #password encoding:
        bhashedPassword = hashlib.md5(password.encode())
        hashedPassword = bhashedPassword.hexdigest()

        self.model.addVoter(fullname[0], fullname[1], hashedPassword)
        #self.dialog.quit()
        return None

    def onVoterDelBtnClick(self):
        self.model.delVoter(self.view.getSelectedVoterFullName())
        return None

    def onAddCandidateBtnClick(self):
        self.model.addCandidate(self.view.getSelectedVoterFullName())
        return None

    def candidateDelBtnClick(self):
        self.model.delCandidate(self.view.getSelectedCandidateFullName())
        return None

    def validate(self):
        if self.sanityCheck():
            majTypes = self.view.getMajTypes()
            self.model.setFt_maj(majTypes[0])
            self.model.setSt_maj(majTypes[1])
            self.view.showPasswords(self.passwords)
            self.view.destroyWindow()
        return None

    def sanityCheck(self) -> bool:
        listsLengths = self.model.getListsLengths()
        lengthVoters = listsLengths[0]
        lengthCandidates = listsLengths[1]
        majTypes = self.view.getMajTypes()

        if lengthVoters == 0:
            mb.showerror('Pas d\'électeur', 'Veuillez ajouter au moins 1 électeur')
            return False
        elif lengthCandidates == 0:
            mb.showerror('Pas de candidat', 'Veuillez ajouter au moins 1 candidat')
            return False
        elif majTypes[0] == '' or majTypes[1] == '':
            mb.showerror('Type de majorité invalide', 'Veuillez réessayer en sélectionnant les majorités')
            return False
        else:
            return True
