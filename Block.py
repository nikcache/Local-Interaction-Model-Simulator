from Apartment import Apartment
from random import randrange
from itertools import chain
from random import *

class Block:

    def __init__ (self, neighborhoodKey, blockName):
        self.neighborhood = neighborhoodKey
        self.name = blockName
        self.numApart = randrange(4, 8)
        self.apartmentList = {}
        self.character = ""
        self.genApartment()

    def genApartment(self):
        for i in range(self.numApart):
            apart = Apartment(self, "a" + str(i))
            self.apartmentList["a" + str(i)] = apart

    def getNeighborhood(self):
        return self.neighborhood
    
    def getLowerList(self):
        return self.apartmentList

    def getApartmentList(self):
        return self.apartmentList

    def getFamilyList(self):
        familyList = []
        for key, apartment in self.apartmentList.items():
            familyList.append(list(apartment.getFamilyList().values()))
        familyList = list(chain.from_iterable(familyList))
        return familyList

    def getPersonList(self):
        PersonList = []
        for keyApartment, apartment in self.apartmentList.items():
            for keyFamily, family in apartment.familyList.items():
                PersonList.append(list(family.getPersonList().values()))
        PersonList = list(chain.from_iterable(PersonList))
        return PersonList

    def getUpper(self):
        return self.neighborhood

    def getCity(self):
        return self.neighborhood.city

    def getCharacter(self):
        apartmentCharacterList = {"altruist":0, "egoist":0, "hooligan":0}
        blockCharacter = ""
        possible = ["altruist", "egoist", "hooligan"]

        if self.character == "" or self.getCity().simulate:
        
            for key, apartment in self.apartmentList.items():
                apartmentCharacterList[apartment.getCharacter()] += 1
            
            if apartmentCharacterList["altruist"] < apartmentCharacterList["egoist"]:
                possible.remove("altruist")
            if apartmentCharacterList["altruist"] > apartmentCharacterList["egoist"]:
                possible.remove("egoist")
            if apartmentCharacterList["altruist"] < apartmentCharacterList["hooligan"] and "altruist" in possible:
                possible.remove("altruist")
            if apartmentCharacterList["altruist"] > apartmentCharacterList["hooligan"]:
                possible.remove("hooligan")
            if apartmentCharacterList["hooligan"] < apartmentCharacterList["egoist"] and "hooligan" in possible:
                possible.remove("hooligan")
            if apartmentCharacterList["hooligan"] > apartmentCharacterList["egoist"] and "egoist" in possible:
                possible.remove("egoist")

            blockCharacter = choice(possible)

            self.character = blockCharacter
            return blockCharacter

        else:
            return self.character

    def getType(self, sVal):
        if sVal == "up":
            return "n"
        elif sVal == "here":
            return "b"
        elif sVal == "down":
            return "a"


def main(): 
    block = Block(1,"test") 
    block.genApartment()
    print(block.getPersonList())
    print(block.getFamilyList())
    print(len(block.getApartmentList()))
    print(len(block.getPersonList()))
    print(len(block.getFamilyList()))
    print(block.getCharacter())

if __name__ == "__main__": 
    main() 