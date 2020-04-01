#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the view of the Admin GUI. There, we will update the GUI, and send events to
# the controller.
#
from tkinter import * #we need to install that lib beforehand (apt ... python3-tk)
from tkinter import ttk
import admincontroller

class Adminview():

    def __init__(self):
        ctrl = admincontroller.Admincontroller()
        self.createAndShowWindow()
        return None

    def createAndShowWindow(self):
        window = Tk()
        window.title('PeopleVoice - Mode Admin')

        majFrame = LabelFrame(window, text="Type de majorité")
        majTypeFirstTurn = Label(majFrame, text='Type de majorité du \n premier tour')
        majTypeScdTurn = Label(majFrame, text='Type de majorité du \n premier tour')
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

        votersFrame = LabelFrame(window, text='Electeurs')
        votersLabel = Label(votersFrame, text='Electeurs')
        votersLabel.grid(column=0, row=0)
        self.votersList = Listbox(votersFrame)
        self.votersList.grid(column=0, row=1, rowspan=4)
        voterAddBtn = Button(votersFrame, text='Ajouter un électeur', command=self.onVoterAddBtnClick)
        voterAddBtn.grid(column=1, row=3)
        voterDelBtn = Button(votersFrame, text='Supprimer un électeur', command=self.onVoterDelBtnClick)
        voterDelBtn.grid(column=1, row=4)
        votersFrame.grid(column=0, row=1)

        candidatesFrame = LabelFrame(window, text='Candidats')
        self.candidatesList = Listbox(candidatesFrame)
        self.candidatesList.grid(column=0, columnspan=2, row=0, rowspan=6)

        candidateAddBtn = Button(candidatesFrame, text='Ajouter un candidat', command=self.onAddCandidateBtnClick)
        candidateAddBtn.grid(column=0, row=6)
        candidateDelBtn = Button(candidatesFrame, text='Supprimer un candidat', command=self.onDelCandidateBtnClick)
        candidateDelBtn.grid(column=0, row=7)
        candidatesFrame.grid(column=1, row=0, rowspan=2)

        validateBtn = Button(window, text='Valider', command=self.validate)
        validateBtn.grid(column=1, row=2)

        window.mainloop()
        return None

    def setVotersListContent(self, content:list):
        ## TODO
        return None

    def setCandidatesList(self, content:list):
        ## TODO
        return None

    def onVoterAddBtnClick(self):
        ## TODO
        return None

    def onVoterDelBtnClick(self):
        ## TODO
        return None

    def onAddCandidateBtnClick(self):
        ## TODO
        return None

    def onDelCandidateBtnClick(self):
        ## TODO
        return None

    def validate(self):
        ## TODO
        return None
