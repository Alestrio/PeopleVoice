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

    def setCandidatesId(self):
        ## TODO:setCandidatesId
        return None

    def getAdminIdentifier(self) -> str:
        return self.properties.get('adminid')

    def getAdminPWHash(self) -> str:
        return self.properties.get('adminpwhash')
