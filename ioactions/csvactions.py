#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import csv

class CsvActions:

    #Constructor
    def __init__(self, path:str):
        self.PATH = path
        with open(self.PATH, newline='') as csvfile:
            self.votersReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            self.votersWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        return None

    def setPath(self, topath:str):
        self.PATH = topath;
        return None

    def addLine(self, forename:str, lastname:str, password:str, vote1:int, vote2:int): #Votes are int because the ID of the given person is specified
        self.votersWriter.writerow([forename, lastname, password, vote1, vote2])
        #TODO Hashing the PW
        return None

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
        return None

    def getAllLines(self) -> list:
        votersList = list();
        for row in self.votersReader:
            votersList.append(row)
        return votersList

    def writeRowsToCsv(self, rows:list):
        votersWriter.writerows(rows)
        return None

    def delById(self, id:int):
        votersList = self.getAllLines()
        votersList.remove(votersList[id])
        self.writeRowsToCsv(votersList)
        return None

    #debug function
    def sayHi(self):
        print('hi')
        return None
