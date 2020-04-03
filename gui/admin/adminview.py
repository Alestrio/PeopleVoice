#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import * #we need to install that lib beforehand (apt ... python3-tk)
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
        for voter in self.model.getVoters():
            self.votersList.insert(0, voter[0] + ' ' + voter[1])
        self.votersList.grid(column=0, row=1, rowspan=4)
        voterAddBtn = Button(votersFrame, text='Ajouter un électeur', command=self.onVoterAddBtnClick)
        voterAddBtn.grid(column=1, row=3)
        voterDelBtn = Button(votersFrame, text='Supprimer un électeur', command=self.onVoterDelBtnClick)
        voterDelBtn.grid(column=1, row=4)
        votersFrame.grid(column=0, row=1)

        candidatesFrame = LabelFrame(self.window, text='Candidats')
        self.candidatesList = Listbox(candidatesFrame)
        self.candidatesList.grid(column=0, columnspan=2, row=0, rowspan=6)
        candidateAddBtn = Button(candidatesFrame, text='Ajouter un candidat', command=self.onAddCandidateBtnClick)
        candidateAddBtn.grid(column=0, row=6)
        candidateDelBtn = Button(candidatesFrame, text='Supprimer un candidat', command=self.onDelCandidateBtnClick)
        candidateDelBtn.grid(column=0, row=7)
        candidatesFrame.grid(column=1, row=0, rowspan=2)

        validateBtn = Button(self.window, text='Valider', command=self.window.quit)
        validateBtn.grid(column=1, row=2)

        self.window.mainloop()
        return None

    def setVotersListContent(self, content:list):
        #On efface et remet le contenu de la listbox de façon à éviter les doublons
        self.votersList.delete(0, END)
        for voter in self.model.getVoters():
            self.votersList.insert(0, voter[0] + ' ' + voter[1])
        return None

    def setCandidatesList(self, content:list):
        #On efface et remet le contenu de la listbox de façon à éviter les doublons
        self.candidatesList.delete(0, END)
        self.candidatesList.insert(content)
        return None

    def onVoterAddBtnClick(self):
        self.controller.onVoterAddBtnClick()
        return None

    def onVoterDelBtnClick(self):
        self.ctrl.voterDelBtnClick()
        return None

    def onAddCandidateBtnClick(self):
        self.ctrl.candidateAddBtnClick()
        return None

    def onDelCandidateBtnClick(self):
        self.ctrl.candidateDelBtnClick()
        return None
