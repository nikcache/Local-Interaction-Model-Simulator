from Neighborhood import Neighborhood
from random import randrange
from itertools import chain 

class City:

    def __init__ (self):
        self.numNeighborhood = randrange(2, 5)
        self.neighborhoodList = {}
        self.character = ""
        self.genNeigh()
        self.simulate = False

    def getCity(self):
        return self
    
    def genNeigh(self):
        for i in range(self.numNeighborhood):
            neigh = Neighborhood(self, "n" + str(i))
            self.neighborhoodList["n" + str(i)] = neigh

    def getNeighborhoodList(self):
        return self.neighborhoodList

    def getLowerList(self):
        return self.neighborhoodList

    def getBlockList(self):
        blockList = []
        for key, neighbor in self.neighborhoodList.items():
            blockList.append(list(neighbor.getBlockList().values()))
        blockList = list(chain.from_iterable(blockList))
        return blockList

    def getApartmentList(self):
        apartmentList = []
        for key, neighbor in self.neighborhoodList.items():
            for key, block in neighbor.blockList.items():
                apartmentList.append(list(block.getApartmentList().values()))
        apartmentList = list(chain.from_iterable(apartmentList))
        return apartmentList

    def getFamilyList(self):
        familyList = []
        for key, neighbor in self.neighborhoodList.items():
            for key, block in neighbor.blockList.items():
                for key, apartment in block.apartmentList.items():
                    familyList.append(list(apartment.getFamilyList().values()))
        familyList = list(chain.from_iterable(familyList))
        return familyList

    def getPersonList(self):
        PersonList = []
        for key, neighbor in self.neighborhoodList.items():
            for key, block in neighbor.blockList.items():
                for keyApartment, apartment in block.apartmentList.items():
                    for keyFamily, family in apartment.familyList.items():
                        PersonList.append(list(family.getPersonList().values()))
        PersonList = list(chain.from_iterable(PersonList))
        return PersonList

    def getCharacter(self):
        neighborhoodCharacterList = {"altruist":0, "egoist":0, "hooligan":0}
        cityCharacter = ""
        possible = ["altruist", "egoist", "hooligan"]

        if self.character == "" or self.simulate:
        
            for key, neighborhood in self.neighborhoodList.items():
                neighborhoodCharacterList[neighborhood.getCharacter()] += 1
            
            if neighborhoodCharacterList["altruist"] < neighborhoodCharacterList["egoist"]:
                possible.remove("altruist")
            if neighborhoodCharacterList["altruist"] > neighborhoodCharacterList["egoist"]:
                possible.remove("egoist")
            if neighborhoodCharacterList["altruist"] < neighborhoodCharacterList["hooligan"] and "altruist" in possible:
                possible.remove("altruist")
            if neighborhoodCharacterList["altruist"] > neighborhoodCharacterList["hooligan"]:
                possible.remove("hooligan")
            if neighborhoodCharacterList["hooligan"] < neighborhoodCharacterList["egoist"] and "hooligan" in possible:
                possible.remove("hooligan")
            if neighborhoodCharacterList["hooligan"] > neighborhoodCharacterList["egoist"] and "egoist" in possible:
                possible.remove("egoist")

            cityCharacter = choice(possible)

            self.character = cityCharacter
            return cityCharacter

        else:
            return self.character

    def getType(self, sVal):
        if sVal == "up":
            return "q"
        elif sVal == "here":
            return "c"
        elif sVal == "down":
            return "n"

def main(): 
    city = City() 
    city.genNeigh()
    #print(city.getPersonList())
    #print(city.getFamilyList())
    print(len(city.getPersonList()))
    print(len(city.getFamilyList()))
    print(len(city.getApartmentList()))
    print(len(city.getBlockList()))
    print(len(city.getNeighborhoodList()))
    print(city.getCharacter())

if __name__ == "__main__": 
    main() 

    
    print(len(city.getBlockList()))
    print(len(city.getNeighborhoodList()))
    print(city.getCharacter())

    