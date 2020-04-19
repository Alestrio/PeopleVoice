#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import *

class Studentview:

    def __init__(self):

        return None

    def createAndShowWindow(self):
        self.window = Tk()
        self.window.title('PeopleVoice - Mode Electeur')

        pwFrame = LabelFrame(self.window, text='Identification')
        pwLabel = Label(pwFrame, text='Mot de passe :')
        pwTextField = Entry(pwFrame)
        pwValidateBtn = Button(pwFrame, text='Valider', command=self.pwValidate)
        fullnameInfoLabel = Label(pwFrame, text='Nom / Prénom')
        self.fullnameLabel = Label(pwFrame)
        pwLabel.grid(column=0, row=0)
        pwTextField.grid(column=1, row=0)
        pwValidateBtn.grid(column=2, row=0)
        fullnameInfoLabel.grid(column=0, row=1)
        self.fullnameLabel.grid(column=1, row=1)

        listsFrame = LabelFrame(self.window, text='Sélection')
        candidatesLabel = Label(listsFrame, text='Candidats')
        votersLabel = Label(listsFrame, text='Electeurs')
        self.candidatesList = Listbox(listsFrame)
        self.setCandidatesListContent()
        self.votersList = Listbox(listsFrame)
        self.setVotersListContent()
        candidatesLabel.grid(column=0, row=0)
        votersLabel.grid(column=1, row=0)
        self.candidatesList.grid(column=0, row=1)
        self.votersList.grid(column=1, row=1)

        choiceFrame = LabelFrame(self.window, text='Choix')
        fcInfoLabel = Label(choiceFrame, text='Choix 1 :')
        self.fcLabel = Label(choiceFrame)
        scInfoLabel = Label(choiceFrame, text='Choix 2 :')
        self.scLabel = Label(choiceFrame)
        fcInfoLabel.grid(row=0, column=0)
        self.fcLabel.grid(row=0, column=1)
        scInfoLabel.grid(row=1, column=0)
        self.scLabel.grid(row=1, column=1)

        actionsFrame = Frame(self.window)
        turnOkBtn = Button(actionsFrame, text='Terminer', command=self.turnOk)
        sessionOkBtn = Button(actionsFrame, text='Terminer la session (admin)', command=self.sessionOk)
        turnOkBtn.pack()
        sessionOkBtn.pack()

        pwFrame.grid(row=0, column=0)
        listsFrame.grid(row=1, column=0)
        choiceFrame.grid(row=0, column=1)
        actionsFrame.grid(row=1, column=1)

        self.window.mainloop()

        return None

    def pwValidate(self):
        print(hello)
        return None

    def turnOk(self):

        return None

    def sessionOk(self):

        return None

    def setCandidatesListContent(self):

        return None

    def setVotersListContent(self):

        return None
