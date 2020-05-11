#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import studentview
import studentcontroller
import sys
sys.path.insert(0, "../../ioactions") #We need to use sys because those are in
import csvactions as csva             #another folder
import settings as sett

class Student:

    def __init__(self):
        self.controller = studentcontroller.Studentcontroller(self)
        self.view = studentview.Studentview(self)
        self.st = sett.Settings('settings.yaml') #if we want to move the voters
        csvpath = self.st.getCsvPath()                 #file to another folder
        self.controller.setView()
        self.csv = csva.CsvActions(csvpath)
        self.forceSecTurn = False
        self.view.createAndShowWindow()
        return None

    def getVoterRow(self, password):
        id = self.csv.linkPasswordAndId(password)
        if id != -1:
            self.currentVoter = self.csv.getById(id)
            self.view.updateVoterInfos()
        else:
            print('Aucun utilisateur avec ce mot de passe')
        return id

    def setChoiceOne(self, choice:str):
        id = self.csv.linkNameAndId(choice)
        voterId = self.csv.linkNameAndId(self.currentVoter[0] + ' ' + self.currentVoter[1])
        self.csv.setChoiceOne(id, voterId, self.forceSecTurn)
        self.view.updateChoiceOneInfos(choice)
        return None

    def setChoiceTwo(self, choice:str):
        id = self.csv.linkNameAndId(choice)
        voterId = self.csv.linkNameAndId(self.currentVoter[0] + ' ' + self.currentVoter[1])
        self.csv.setChoiceTwo(id, voterId, self.forceSecTurn)
        self.view.updateChoiceTwoInfos(choice)
        return None

    def endSession(self):
        self.view.destroyWindow()
        return None

    def getVoters(self):
        return self.csv.getAllLines()

    def getCandidates(self):
        fullnames = ''
        if self.st.getCandidatesId() != None:
            ids = self.st.getCandidatesId().split(" ")#[1:]
            fullnames = self.csv.linkIdAndNames(ids)
        return fullnames

    def clearCurrentVoter(self):
        self.currentVoter = None
        return None
