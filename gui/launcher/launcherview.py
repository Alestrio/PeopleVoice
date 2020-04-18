#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# We are not using controller there because it's a very simple window....
#
from tkinter import *

class Launcherview:

    def __init__(self, model):
        self.model = model
        return None

    def createAndShowWindow(self):
        self.window = Tk()
        adminBtn = Button(self.window, text='Mode Admin', command=self.adminBtnClick)
        adminBtn.pack()
        studentBtn = Button(self.window, text="Mode Elève", command=self.studentBtnClick)
        studentBtn.pack()
        resultBtn = Button(self.window, text='Mode résultats', command=self.resultBtnClick)
        resultBtn.pack()
        self.window.mainloop()
        return None

    def adminBtnClick(self):
        self.model.startAdminMode()
        return None

    def studentBtnClick(self):
        self.model.startStudentMode()
        return None

    def resultBtnClick(self):
        self.model.startResultMode()
        return None
