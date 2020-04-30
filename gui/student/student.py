#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import studentview
import studentcontroller
sys.path.insert(0, "../../ioactions") #We need to use sys because those are in
import csvactions as csva             #another folder
import settings as sett

class Student:

    def __init__(self):
        self.controller = studentcontroller.Studentcontroller(self)
        self.view = studentview.Studentview(self)
        self.view.createAndShowWindow()
        self.st = sett.Settings('settings.yaml') #if we want to move the voters
        csvpath = self.st.getCsvPath()                 #file to another folder
        self.csv = csva.CsvActions(csvpath)
        return None

    def getVoterRow(self, password):
        id = self.csv.linkPasswordAndId(password)
        if id != -1:
            self.currentVoter = self.csv.getById(id)
            self.view.updateVoterInfos()
        else:
            print('No user corresponding to that password')
        return id

    def setChoiceOne(self, choice:str):
        id = self.csv.linkNameAndId(choice)
        voterId = self.csv.linkNameAndId(self.currentVoter[0] + ' ' + self.currentVoter[1])
        self.csv.setChoiceOne(id, voterId)
        return None

    def setChoiceTwo(self, choice:str):
        id = self.csv.linkNameAndId(choice)
        self.csv.setChoiceTwo(id)
        return None
