#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import sys
sys.path.insert(0, "ioactions")
sys.path.insert(0, "gui/launcher")

import csvactions as csvactions
import settings as settings
import launcher

sett = settings.Settings('settings.yaml')
launch = launcher.Launcher()
#csvpath = ""
#settingspath = ""

def isFirstRun() -> bool:
    if sett.isAdminIdNull() and sett.isAdminPWNull():
        return True
    else:
        return False

if isFirstRun():
    launch.startFirstRun()
else:
    launch.startLauncher()
