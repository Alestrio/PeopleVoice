#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
#
import yaml

class Settings():

    def __init__(self, path:str):
        self.PATH = path
        with open(self.PATH, "r") as yamlfile:
            self.properties = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return None

    def getCandidatesId(self) -> list:
        return self.properties.get("candidates")

    def setCandidatesId(self, candidates:str):
        self.properties['candidates'] = candidates
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile)
        return None

    def getAdminIdentifier(self) -> str:
        return self.properties.get('adminid')

    def getAdminPWHash(self) -> str:
        return self.properties.get('adminpwhash')

    def getCsvPath(self) -> str:
        return self.properties.get('csvpath')

    def addCandidateByFullName(self, fullname:str, votersList:list):
        newContent = ''
        current = self.getCandidatesId()
        names = fullname.split(" ")
        forename = names[0]
        lastname = names[1]
        id = -1
        for line in votersList:
            if forename == line[0] and lastname == line[1]:
                id = votersList.index(line)
        items = current.split(" ")
        for i in items:
            newContent += i + " "
        newContent += str(id)
        self.setCandidatesId(newContent)
        return None
