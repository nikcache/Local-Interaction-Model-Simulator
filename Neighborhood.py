from Block import Block
from random import randrange
from itertools import chain 
from random import *

class Neighborhood:

    def __init__ (self, cityKey, neighborhoodName):
        self.city = cityKey
        self.name = neighborhoodName
        self.numBlock = randrange(5, 8)
        self.blockList = {}
        self.character = ""
        self.genBlock()

    def genBlock(self):
        for i in range(self.numBlock):
            block = Block(self, "b" + str(i))
            self.blockList["b" + str(i)] = block

    def getBlockList(self):
        return self.blockList

    def getLowerList(self):
        return self.blockList

    def getApartmentList(self):
        apartmentList = []
        for key, block in self.blockList.items():
            apartmentList.append(list(block.getApartmentList().values()))
        apartmentList = list(chain.from_iterable(apartmentList))
        return apartmentList

    def getFamilyList(self):
        familyList = []
        for key, block in self.blockList.items():
            for key, apartment in block.apartmentList.items():
                familyList.append(list(apartment.getFamilyList().values()))
        familyList = list(chain.from_iterable(familyList))
        return familyList

    def getPersonList(self):
        PersonList = []
        for key, block in self.blockList.items():
            for keyApartment, apartment in block.apartmentList.items():
                for keyFamily, family in apartment.familyList.items():
                    PersonList.append(list(family.getPersonList().values()))
        PersonList = list(chain.from_iterable(PersonList))
        return PersonList

    def getUpper(self):
        return self.city

    def getCity(self):
        return self.city

    def getCharacter(self):
        blockCharacterList = {"altruist":0, "egoist":0, "hooligan":0}
        neighborhoodCharacter = ""
        possible = ["altruist", "egoist", "hooligan"]

        if self.character == "" or self.getCity().simulate:
        
            for key, block in self.blockList.items():
                blockCharacterList[block.getCharacter()] += 1
            
            if blockCharacterList["altruist"] < blockCharacterList["egoist"]:
                possible.remove("altruist")
            if blockCharacterList["altruist"] > blockCharacterList["egoist"]:
                possible.remove("egoist")
            if blockCharacterList["altruist"] < blockCharacterList["hooligan"] and "altruist" in possible:
                possible.remove("altruist")
            if blockCharacterList["altruist"] > blockCharacterList["hooligan"]:
                possible.remove("hooligan")
            if blockCharacterList["hooligan"] < blockCharacterList["egoist"] and "hooligan" in possible:
                possible.remove("hooligan")
            if blockCharacterList["hooligan"] > blockCharacterList["egoist"] and "egoist" in possible:
                possible.remove("egoist")

            neighborhoodCharacter = choice(possible)

            self.character = neighborhoodCharacter
            return neighborhoodCharacter

        else:
            return self.character

    def getType(self, sVal):
        if sVal == "up":
            return "c"
        elif sVal == "here":
            return "n"
        elif sVal == "down":
            return "b"

def main(): 
    nei = Neighborhood(1,"test") 
    nei.genBlock()
    print(nei.getPersonList())
    print(nei.getFamilyList())
    print(len(nei.getPersonList()))
    print(len(nei.getFamilyList()))
    print(len(nei.getApartmentList()))
    print(len(nei.getBlockList()))
    print(nei.getCharacter())

if __name__ == "__main__": 
    main() 
