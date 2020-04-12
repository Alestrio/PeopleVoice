#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
# Hey Alex
import admincontroller
import adminview
import sys
sys.path.insert(0, "../../ioactions") #We need to use sys because those are in
import csvactions as csva             #another folder
import settings as sett

class Admin:

    def __init__(self):
        self.st = sett.Settings('settings.yaml') #if we want to move the voters
        csvpath = self.st.getCsvPath()                 #file to another folder
        self.csv = csva.CsvActions(csvpath)

        self.view = adminview.Adminview(self)
        self.view.createAndShowWindow()
        return None

    def addVoter(self, forename:str, lastname:str, passwordhash:str):
        self.csv.addLine(forename, lastname, passwordhash, -1, -1) #vote to -1 to
        self.view.setVotersListContent()        #assert that no
        return None                                 #vote has been done


    def delVoter(self, fullname:str):
        self.csv.delByFullName(fullname)
        self.view.setVotersListContent()
        return None

    def getVoters(self) -> list:
        lines = self.csv.getAllLines()
        return lines

    def addCandidate(self, fullname:str):
        votersList = self.getVoters()
        self.st.addCandidateByFullName(fullname, votersList)
        self.view.setCandidatesList()
        return None

    def delCandidate(self, fullname:str):
        id = self.csv.linkNameAndId(fullname)
        if id != -1:
            self.st.delCandidateById(id)
            self.view.setCandidatesList()
        else:
            print("Error : candidate id = -1")
        return None

    def getCandidates(self):
        ids = self.st.getCandidatesId().split(" ")#[1:]
        fullnames = self.csv.linkIdAndNames(ids)
        return fullnames

#We'll add methods to edit voters maybe later. Now, we focus on creating a
#simple but robust app. Furthermore, ideally, we can move the definition of
#the settings file to a global variable somewhere in the code.
