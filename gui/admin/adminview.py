#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import * #we need to install that lib beforehand (apt ... python3-tk)
from tkinter import messagebox as mb
import admincontroller

class Adminview():

    def __init__(self, model):
        self.model = model
        self.controller = admincontroller.Admincontroller(self, model)
        return None

    def createAndShowWindow(self):
        self.window = Tk()
        self.window.title('PeopleVoice - Mode Admin')

        majFrame = LabelFrame(self.window, text="Type de majorité")
        majTypeFirstTurn = Label(majFrame, text='Type de majorité du \n premier tour')
        majTypeScdTurn = Label(majFrame, text='Type de majorité du \n second tour')
        majTypeFirstTurn.grid(column=0, row=0)
        majTypeScdTurn.grid(column=1, row=0)
        self.FT_maj = StringVar()
        #FT stands for First Turn
        FT_absoluteMaj = Radiobutton(majFrame, text='Absolue', variable=self.FT_maj, value='absolute')
        FT_absoluteMaj.grid(column=0, row=1)
        FT_relativeMaj = Radiobutton(majFrame, text='Relative', variable=self.FT_maj, value='relative')
        FT_relativeMaj.grid(column=0, row=2)
        #ST stands for Second Turn
        self.ST_maj = StringVar()
        ST_absoluteMaj = Radiobutton(majFrame, text='Absolue', variable=self.ST_maj, value='absolute')
        ST_absoluteMaj.grid(column=1, row=1)
        ST_relativeMaj = Radiobutton(majFrame, text='Relative', variable=self.ST_maj, value='relative')
        ST_relativeMaj.grid(column=1, row=2)
        majFrame.grid(column=0, row=0)

        votersFrame = LabelFrame(self.window, text='Electeurs')
        self.votersList = Listbox(votersFrame)
        self.setVotersListContent()
        self.votersList.grid(column=0, row=1, rowspan=4)
        voterAddBtn = Button(votersFrame, text='Ajouter un électeur', command=self.createVoterAddWindow)
        voterAddBtn.grid(column=1, row=3)
        voterDelBtn = Button(votersFrame, text='Supprimer un électeur', command=self.controller.onVoterDelBtnClick)
        voterDelBtn.grid(column=1, row=4)
        votersFrame.grid(column=0, row=1)

        candidatesFrame = LabelFrame(self.window, text='Candidats')
        self.candidatesList = Listbox(candidatesFrame)
        self.candidatesList.grid(column=0, columnspan=2, row=0, rowspan=6)
        self.setCandidatesList()
        candidateAddBtn = Button(candidatesFrame, text='Ajouter un candidat', command=self.controller.onAddCandidateBtnClick)
        candidateAddBtn.grid(column=0, row=6)
        candidateDelBtn = Button(candidatesFrame, text='Supprimer un candidat', command=self.controller.candidateDelBtnClick)
        candidateDelBtn.grid(column=0, row=7)
        candidatesFrame.grid(column=1, row=0, rowspan=2)

        validateBtn = Button(self.window, text='Valider', command=self.controller.validate)
        validateBtn.grid(column=1, row=2)

        self.window.mainloop()
        return None

    def setVotersListContent(self):
        #On efface et remet le contenu de la listbox de façon à éviter les doublons
        self.votersList.delete(0, END)
        for voter in self.model.getVoters():
            self.votersList.insert(0, voter[0] + ' ' + voter[1])
        return None

    def setCandidatesList(self):
        #On efface et remet le contenu de la listbox de façon à éviter les doublons
        self.candidatesList.delete(0, END)
        for fullname in self.model.getCandidates():
            self.candidatesList.insert(0, fullname)
        return None

    def getSelectedVoterFullName(self):
        return self.votersList.get(self.votersList.curselection())

    def getSelectedCandidateFullName(self):
        return self.candidatesList.get(self.candidatesList.curselection())

    def getMajTypes(self):
        return (self.FT_maj.get(), self.ST_maj.get())

    def destroyWindow(self):
        self.window.destroy()
        return None

    def showPasswords(self, passwords:list):
        dialog = Tk()
        dialog.title('PeopleVoice - Mots de passe')
        content = 'Utilisateur :: Mot de passe\n'
        for pw in passwords:
            content = content + pw + '\n'
        passLabel = Label(dialog, text=content)
        passLabel.pack()
        dialog.mainloop()
        return None

    def createVoterAddWindow(self):
        dialog = Tk()
        self.forenameEntry = Entry(dialog)
        self.lastnameEntry = Entry(dialog)
        dialog.title('PeopleVoice - Ajouter un électeur')

        forenameLabel = Label(dialog, text='Prénom :')
        forenameLabel.grid(column=0, row=0)
        self.forenameEntry.grid(column=1, row=0)

        lastnameLabel = Label(dialog, text='Nom :')
        lastnameLabel.grid(column=0, row=1)
        self.lastnameEntry.grid(column=1, row=1)

        validatebtn = Button(dialog, text='Valider', command=self.controller.validateAddVoter)
        validatebtn.grid(column=1, row=2)
        dialog.mainloop()
        return None

    def getNewVoterFullname(self):
        return (self.forenameEntry.get(), self.lastnameEntry.get())
