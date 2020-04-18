#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import launcherview
import settings as settings


import sys
sys.path.insert(0, "ioactions")
sys.path.insert(0, "gui/admin")
sys.path.insert(0, "gui/configurator")
sys.path.insert(0, "gui/adminlogin")
import admin
import adminlogin
import configurator

class Launcher:

    def __init__(self):
        self.view = launcherview.Launcherview(self)
        self.sett = settings.Settings('settings.yaml') # TODO path in a global var
        return None

    def startLauncher(self):
        self.view.createAndShowWindow()
        return None

    def startAdminMode(self):
        self.view.window.destroy()
        adminlog = adminlogin.Adminlogin(self.sett.getAdminPWHash(), self.sett.getAdminIdentifier())
        if adminlog.isAccessGranted():
            adm = admin.Admin()
        return None

    def startFirstRun(self):
        config =  configurator.Configurator()
        if config.hasSucceeded():
            adminlog = adminlogin.Adminlogin(self.sett.getAdminPWHash(), self.sett.getAdminIdentifier())
            if adminlog.isAccessGranted():
                adm = admin.Admin()
        return None

    def startResultMode(self):

        return None

    def startStudentMode(self):

        return None
