#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import *

class Studentview:

    def __init__(self, model):
        self.model = model
        self.controller = model.controller
        return None

    def createAndShowWindow(self):
        self.window = Tk()
        self.window.title('PeopleVoice - Mode Electeur')

        pwFrame = LabelFrame(self.window, text='Identification')
        pwLabel = Label(pwFrame, text='Mot de passe :')
        self.pwTextField = Entry(pwFrame)
        pwValidateBtn = Button(pwFrame, text='Valider', command=self.controller.pwValidate)
        fullnameInfoLabel = Label(pwFrame, text='Nom / Prénom')
        self.fullnameLabel = Label(pwFrame)
        pwLabel.grid(column=0, row=0)
        self.pwTextField.grid(column=1, row=0)
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
        setChoice1Btn = Button(actionsFrame, text='Selectionner comme premier choix', command=self.controller.selectAsChoiceOne)
        setChoice2Btn = Button(actionsFrame, text='Selectionner comme second choix', command=self.controller.selectAsChoiceTwo)
        choiceOkBtn = Button(actionsFrame, text='Terminer le choix', command=self.controller.choiceOk)
        turnOkBtn = Button(actionsFrame, text='Terminer le tour (admin)', command=self.controller.turnOk)
        sessionOkBtn = Button(actionsFrame, text='Terminer la session (admin)', command=self.controller.sessionOk)
        setChoice1Btn.pack()
        setChoice2Btn.pack()
        choiceOkBtn.pack()
        turnOkBtn.pack()
        sessionOkBtn.pack()

        pwFrame.grid(row=0, column=0)
        listsFrame.grid(row=1, column=0)
        choiceFrame.grid(row=0, column=1)
        actionsFrame.grid(row=1, column=1)

        self.window.mainloop()

        return None

    def getPasswordEntry(self):
        return self.pwTextField.get()

    def updateVoterInfos(self):
        self.fullnameLabel['text'] = self.model.currentVoter[0] + ' ' + self.model.currentVoter[1]
        return None

    def clearVoterInfos(self):
        self.fullnameLabel['text'] = ''
        self.pwTextField.delete(0, 'end')
        return None

    def setCandidatesListContent(self):
        self.candidatesList.delete(0, END)
        for fullname in self.model.getCandidates():
            self.candidatesList.insert(0, fullname)
        return None

    def setVotersListContent(self):
        self.votersList.delete(0, END)
        for voter in self.model.getVoters():
            self.votersList.insert(0, voter[0] + ' ' + voter[1])
        return None

    def getVotersListSelection(self):
        if self.votersList.curselection() != '':
            return self.votersList.get('active')
        else:
            return None

    def getCandidatesListSelection(self):
        if self.candidatesList.curselection() != '':
            return self.candidatesList.get('active')
        else:
            return None

    def updateChoiceOneInfos(self, choiceName:str):
        self.fcLabel['text'] = choiceName
        return None

    def updateChoiceTwoInfos(self, choiceName:str):
        self.scLabel['text'] = choiceName
        return None

    def destroyWindow(self):
        self.window.destroy()
        return None

    def clearChoicesInfos(self):
        self.fcLabel['text'] = ''
        self.scLabel['text'] = ''
        return None
