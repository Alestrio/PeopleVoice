#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import studentview
class Student:

    def __init__(self):
        view = studentview.Studentview()
        view.createAndShowWindow()
        return None
