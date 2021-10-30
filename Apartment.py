from Family import Family
from random import *
from itertools import chain 

class Apartment:

    def __init__ (self, blockKey, apartmentName):
        self.name = apartmentName
        self.numFamily = randrange(4, 10)
        self.familyList = {}
        self.genFamily()
        self.character = ""
        self.block = blockKey

    def genFamily(self):
        for i in range(self.numFamily):
            family = Family(self, "family" + str(i))
            self.familyList["f" + str(i)] = family

    def getLowerList(self):
        return self.familyList

    def getFamilyList(self):
        return self.familyList

    def getPersonList(self):
        personList = []
        for key, family in self.familyList.items():
            personList.append(list(family.getPersonList().values()))
        personList = list(chain.from_iterable(personList))
        return personList

    def getUpper(self):
        return self.block

    def getBlock(self):
        return self.block

    def getNeighborhood(self):
        return self.block.neighborhood

    def getCity(self):
        return self.block.neighborhood.city

    def getCharacter(self):
        familyCharacterList = {"altruist":0, "egoist":0, "hooligan":0}
        apartmentCharacter = ""
        possible = ["altruist", "egoist", "hooligan"]

        if self.character == "" or self.getCity().simulate:
        
            for key, family in self.familyList.items():
                familyCharacterList[family.getCharacter()] += 1
            
            if familyCharacterList["altruist"] < familyCharacterList["egoist"]:
                possible.remove("altruist")
            if familyCharacterList["altruist"] > familyCharacterList["egoist"]:
                possible.remove("egoist")
            if familyCharacterList["altruist"] < familyCharacterList["hooligan"] and "altruist" in possible:
                possible.remove("altruist")
            if familyCharacterList["altruist"] > familyCharacterList["hooligan"]:
                possible.remove("hooligan")
            if familyCharacterList["hooligan"] < familyCharacterList["egoist"] and "hooligan" in possible:
                possible.remove("hooligan")
            if familyCharacterList["hooligan"] > familyCharacterList["egoist"] and "egoist" in possible:
                possible.remove("egoist")

            apartmentCharacter = choice(possible)

            self.character = apartmentCharacter
            return apartmentCharacter

        else:
            return self.character

    def getType(self, sVal):
        if sVal == "up":
            return "b"
        elif sVal == "here":
            return "a"
        elif sVal == "down":
            return "f"


    
    def __str__(self):
        apartment_fam = ''  
        for familyNum in self.familyList:
            apartment_fam += familyNum + "\n" + self.familyList[familyNum].__str__() +"\n" 
        return apartment_fam 

def main(): 
    apartment = Apartment(10, 'Abi') 
    apartment.genFamily()
    print(apartment.getCharacter())
    #print(len(apartment.getPersonList()))
    #print(apartment.getLowerList())

if __name__ == "__main__": 
    main() 