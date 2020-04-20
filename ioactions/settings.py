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

    def reload(self):
        with open(self.PATH, "r") as yamlfile:
            self.properties = yaml.load(yamlfile, Loader=yaml.FullLoader)

    def getCandidatesId(self) -> list:
        return self.properties.get("candidates")

    def setCandidatesId(self, candidates:str):
        self.properties['candidates'] = candidates
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile) # TODO: method to dump
        return None

    def stringifyCandidates(self, ids:list):
        newValue = ''
        for id in ids:
            newValue += str(id) + " "
        newValue = newValue[:-1]
        return newValue

    def getAdminIdentifier(self) -> str:
        self.reload()
        return self.properties.get('adminid')

    def getAdminPWHash(self) -> str:
        self.reload()
        return self.properties.get('adminpw')

    def getCsvPath(self) -> str:
        self.reload()
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
        if self.getCandidatesId() != None:
            items = current.split(" ")
        else:
            items = list()
        items.append(str(id))
        self.setCandidatesId(self.stringifyCandidates(items))
        return None

    def delCandidateById(self, id:int):
        ids = self.getCandidatesId()
        ids = ids.split(' ')
        ids.remove(ids[id])
        self.setCandidatesId(self.stringifyCandidates(ids))
        return None

    def setFt_maj(self, maj:str):
        self.properties['ft_maj'] = maj
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile) # TODO: method to dump
        return None

    def setSt_maj(self, maj:str):
        self.properties['st_maj'] = maj
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile) # TODO: method to dump
        return None

    def setAdminId(self, id:str):
        self.properties['adminid'] = id
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile) # TODO: method to dump

    def setAdminPW(self, pw:str):
        self.properties['adminpw'] = pw
        with open(self.PATH, "w") as yamlfile:
            yaml.dump(self.properties, yamlfile) # TODO: method to dump

    def isAdminIdNull(self) -> bool:
        if self.properties['adminid'] == None:
            return True
        else:
            return False

    def isAdminPWNull(self) -> bool:
        if self.properties['adminpw'] == None:
            return True
        else:
            return False


    def clean(self):
        self.setCandidatesId(None)
        return None
