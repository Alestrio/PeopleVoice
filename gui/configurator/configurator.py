#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import configuratorcontroller
import configuratorview
import sys
sys.path.insert(0, "../../ioactions")
import settings as sett
import csvactions as csva 
import hashlib

class Configurator:

    def __init__(self):
        self.st = sett.Settings('settings.yaml')
        csvpath = self.st.getCsvPath()
        self.csv = csva.CsvActions(csvpath)

        controller = configuratorcontroller.Configuratorcontroller(self)
        self.view = configuratorview.Configuratorview(controller)
        self.view.createAndShowWindow()
        return None

    def setAdminId(self, id:str):
        self.st.setAdminId(id)
        return None

    def setAdminPW(self, pw:str):
        bhashedpw = hashlib.md5(pw.encode())
        hashedpw = bhashedpw.hexdigest()
        self.st.setAdminPW(hashedpw)
        return None
