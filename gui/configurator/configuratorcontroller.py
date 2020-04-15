#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the controller. There, we will gather the events from the view, and apply
# the actions related to those events. That class also gather and send data to and from
# the model, who does the computation and the link with the rest of the software.
#


class Configuratorcontroller:

    def __init__(self, model):
        self.model = model
        return None

    def validate(self, id:str, pw:str, confPW:str) -> bool:
        if pw == confPW:
            self.model.setAdminId(id)
            self.model.setAdminPW(pw)
            return True
        else:
            return False
