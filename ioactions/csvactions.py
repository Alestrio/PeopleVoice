#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import csv

class CsvActions():
    PATH = ""

    #Constructor
    def  __init__(self):
        with open(PATH, newline='') as csvfile:
            self.votersReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            self.votersWriter = csv.writer(svfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        return null;

    def setPath(self, topath:str):
        PATH = topath;
        return null;

    def addLine(self, forename:str, lastname:str, password:str, vote1:int, vote2:int): #Votes are int because the ID of the given person is specified
        self.votersWriter.writerow([forename, lastname, password, vote1, vote2])
        #TODO Hashing the PW
        return null;

    def setVote(self, id:int, vote1:int, vote2:int):
        votersList = self.getAllLines()
        item = votersList[id]
        splittedItem = item.split(', ') #We split the string we get by ", " to get one element per list item
        splittedItem[3] = vote1
        splittedItem[4] = vote2
        item = ""
        for i in splittedItem:
            item.append(i + ", ") #We build the string again
        item = item[:-1]
        votersList[id] = item
        self.writeRowsToCsv(votersList)
        return null;

    def getAllLines(self) -> lst:
        votersList = list();
        for row in self.votersReader:
            votersList.append(row)
        return votersList;

    def writeRowsToCsv(self, rows:lst):
        votersWriter.writerows(rows)
        return null;
