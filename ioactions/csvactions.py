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
        fullnames = ''
        if ids != ['']:
            lines = self.getAllLines()
            fullnames = list()
            for id in ids:
                line = lines[int(id)]
                fullnames.append(line[0] + " " + line[1])
        return fullnames

    def linkNameAndId(self, fullname:str):
        names = fullname.split(" ")
        forename = names[0]
        lastname = names[1]
        lines = self.getAllLines()
        id = -1
        for line in lines:
            if forename == line[0] and lastname == line[1]:
                id = lines.index(line)
        return id

    def linkPasswordAndId(self, password):
        id = -1
        voters = self.getAllLines()
        bhashedPw = hashlib.md5(password.encode())
        hashedPw = bhashedUserEntry.hexdigest()
        for voter in voters:
            if hashedPw == voter[2]:
                id = voters.index(voter)
        return id

    def getById(self, id:int):
        voters = self.getAllLines()
        return voters[id]

    def isFirstTurn(self):
        isFirstTurn = False
        voters = self.getAllLines()
        for voter in voters:
            if voter[3] == -1:
                isFirstTurn = True
        return isFirstTurn

    def setChoiceOne(self, id:int, voterId:int):
        voters = self.getAllLines()
        fullname = self.getById(voterId)[0] + ' ' + self.getById(voterId)[1]
        if self.isFirstTurn():
            for voter in voters:
                if (voter[0] + ' ' + voter[1]) == fullname:
                    voter[3] = id
        else:
            for voter in voters:
                if (voter[0] + ' ' + voter[1]) == fullname:
                    voter[5] = id
        self.writeRowsToCsv(voters)
        return None

    def setChoiceTwo(self, id:int, voterId:int):
        voters = self.getAllLines()
        fullname = self.getById(voterId)[0] + ' ' + self.getById(voterId)[1]
        if self.isFirstTurn():
            for voter in voters:
                if (voter[0] + ' ' + voter[1]) == fullname:
                    voter[4] = id
        else:
            for voter in voters:
                if (voter[0] + ' ' + voter[1]) == fullname:
                    voter[6] = id
        self.writeRowsToCsv(voters)
        return None

    def clean(self):
        self.writeRowsToCsv([])
        return None
