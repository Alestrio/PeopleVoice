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
        return votersList

    def writeRowsToCsv(self, rows:list):
        with open(self.PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)
        return None

    def delByFullName(self, fullname:str):
        votersList = self.getAllLines()
        names = fullname.split(" ")
        forename = names[0]
        lastname = names[1]
        tempList = list()
        for line in votersList:
            if not forename == line[0] and not lastname == line[1]:
                tempList.append(line)
        self.writeRowsToCsv(tempList)
        return None

    def linkIdAndNames(self, ids:list):
        lines = self.getAllLines()
        fullnames = list()
        for id in ids:
            line = lines[int(id)]
            fullnames.append(line[0] + " " + line[1])
        return fullnames

    #debug function
    def sayHi(self):
        print('hi')
        return None
