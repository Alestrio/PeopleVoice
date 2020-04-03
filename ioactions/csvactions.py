#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import csv

class CsvActions:

    #Constructor
    def __init__(self, path:str):
        self.PATH = path
        return None

    def setPath(self, topath:str):
        self.PATH = topath;
        return None

    def addLine(self, forename:str, lastname:str, password:str, vote1:int, vote2:int): #Votes are int because the ID of the given person is specified
        lines = self.getAllLines()
        lines.append([forename, lastname, password, vote1, vote2])
        self.writeRowsToCsv(lines)
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
        with open(self.PATH, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                votersList.append(row)
            print(votersList)
        return votersList

    def writeRowsToCsv(self, rows:list):
        with open(self.PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)
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
