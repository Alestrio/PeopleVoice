#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import sys
sys.path.insert(0, "ioactions")
sys.path.insert(0, "gui/admin")
sys.path.insert(0, "gui/configurator")
sys.path.insert(0, "gui/adminlogin")


import csvactions as csvactions
import settings as settings
import admin
import adminlogin
import configurator

sett = settings.Settings('settings.yaml')
#adm = admin.Admin()
#csvpath = ""
#settingspath = ""

def isFirstRun() -> bool:
    if sett.isAdminIdNull() and sett.isAdminPWNull():
        return True
    else:
        return False

if isFirstRun():
    config =  configurator.Configurator()
    adminlog = adminlogin.Adminlogin(sett.getAdminPWHash(),sett.getAdminIdentifier())
else:
    adminlog = adminlogin.Adminlogin(sett.getAdminPWHash(), sett.getAdminIdentifier())
