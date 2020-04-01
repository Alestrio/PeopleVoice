#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import admincontroller
import sys
sys.path.insert(0, "../../ioactions") #We need to use sys because those are in
import csvactions as csva             #another folder
import settings as sett

class Admin:

    def __init__(self):
        st = sett.Settings('../../settings.yaml') #if we want to move the voters
        csvpath = st.getCsvPath()                 #file to another folder
        csv = csva.CsvActions()
        csv.setPath(csvpath)
        return None

    def addVoter(self, forename:str, lastname:str, passwordhash:str):
        csv.addLine(forename, lastname, passwordhash, -1, -1) #vote to -1 to
        return None                                           #assert that no
                                                              #vote has been done

    def delVoter(self, id:int):
        csv.delById(id)
        return None

    def getVoters(self) -> list:
        return csv.getAllLines()

#We'll add methods to edit voters maybe later. Now, we focus on creating a
#simple but robust app. Furthermore, ideally, wecan move the definition of
#the settings file to a global variable somewhere in the code.
