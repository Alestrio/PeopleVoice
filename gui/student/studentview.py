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
        pwValidateBtn = Button(pwFrame, text='Valider', command=self.pwValidate)
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
        setChoice1Btn = Button(actionsFrame, text='Selectionner comme premier choix', command=self.selectAsChoiceOne)
        setChoice2Btn = Button(actionsFrame, text='Selectionner comme second choix', command=self.selectAsChoiceTwo)
        choiceOkBtn = Button(actionsFrame, text='Terminer le choix', command=self.choiceOk)
        turnOkBtn = Button(actionsFrame, text='Terminer le tour', command=self.turnOk)
        sessionOkBtn = Button(actionsFrame, text='Terminer la session (admin)', command=self.sessionOk)
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

    def pwValidate(self):
        password = self.pwTextField.get()
        self.model.getVoterRow(password)
        return None

    def updateVoterInfos(self):
        self.fullnameLabel['text'] = self.model.currentVoter[0] + ' ' + self.model.currentVoter[1]
        return None

    def clearVoterInfos(self):
        self.fullnameLabel['text'] = ''
        return None

    def turnOk(self):
        self.model.forceSecTurn = True
        self.controller.showMbSecondTurn()
        return None

    def choiceOk(self):
        self.clearVoterInfos()
        ## TODO: Apply votes
        return None

    def sessionOk(self):

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

    def selectAsChoiceOne(self):
        if self.votersList.curselection() != '':
            voterSelection = self.votersList.get(self.votersList.curselection())
            self.model.setChoiceOne(voterSelection)
        elif self.candidatesList.curselection() != '':
            candidateSelection = self.candidatesList.get(self.candidatesList.curselection())
            self.model.setChoiceOne(candidateSelection)
        else:
            self.controller.showMbNoChoice()
        return None

    def updateChoiceOneInfos(self, choiceName:str):
        self.fcLabel['text'] = choiceName
        return None

    def selectAsChoiceTwo(self):
        if self.votersList.curselection() != '':
            voterSelection = self.votersList.get(self.votersList.curselection())
            self.model.setChoiceTwo(voterSelection)
        elif self.candidatesList.curselection() != '':
            candidateSelection = self.candidatesList.get(self.candidatesList.curselection())
            self.model.setChoiceTwo(candidateSelection)
        else:
            self.controller.showMbNoChoice()
        return None

    def updateChoiceTwoInfos(self, choiceName:str):
        self.scLabel['text'] = choiceName
        return None

    def destroyWindow(self):
        self.window.destroy()
        return None

    def sanityCheck(self):

        return None
