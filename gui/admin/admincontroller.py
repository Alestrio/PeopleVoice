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

class Admincontroller():

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.passwords = list()
        return None


    def validateAddVoter(self, forename, lastname):
        #password generation:
        password = ''
        for i in range(0,9):
            password += random.choice(string.ascii_letters)
        #Saving that password to display them all at the end of the config
        self.passwords.append(lastname + " " + forename + " " + '::' + " " + password)
        #password encoding:
        bhashedPassword = hashlib.md5(password.encode())
        hashedPassword = bhashedPassword.hexdigest()

        self.model.addVoter(forename, lastname, hashedPassword)
        #self.dialog.quit()
        return None

    def onVoterDelBtnClick(self, fullname:str):
        self.model.delVoter(fullname)
        return None

    def onAddCandidateBtnClick(self, fullname:str):
        self.model.addCandidate(fullname)
        return None

    def candidateDelBtnClick(self, fullname:str):
        self.model.delCandidate(fullname)
        return None

    def validate(self, FT_maj:str, ST_maj:str):
        self.model.setFt_maj(FT_maj)
        self.model.setSt_maj(ST_maj)
        self.view.showPasswords(self.passwords)
        return None
