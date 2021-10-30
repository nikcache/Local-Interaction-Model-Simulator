from Person import Person
from random import randrange
from random import choice
from itertools import chain 

class Family:

    def __init__(self, apartmentKey, familyName):
        self.name = familyName
        self.numPerson = randrange(4, 9)
        self.personList = {}
        self.apartment = apartmentKey
        self.character = ""
        self.genPerson()

    def genPerson(self):
        #Abi's code
        #familyList = ["father", "mother", "child1", "child2", "child3",  "child4"] 
        
        #Nikesh's change
        familyList = ["p0", "p1", "p2", "p3", "p4",  "p5", "p6", "p7", "p8"] 
        character = ["altruist", "egoist", "hooligan"]
        social = ["introvert", "extrovert"]


        for i in range(self.numPerson):
            person = Person(choice(character), choice(social),familyList[i],self)
            self.personList[familyList[i]] = person

    def getLowerList(self):
        return self.personList

    def getPersonList(self):
        return self.personList

    def getPersonList1(self):
        personList = []
        for key, person in self.personList.items():
            personList.append(person)
        return personList

    def getCharacter(self):
        personCharacterList = {"altruist":0, "egoist":0, "hooligan":0}
        possible = ["altruist", "egoist", "hooligan"]
        familyCharacter = ""

        if self.character == "" or self.getCity().simulate:
        
            for key, person in self.personList.items():
                personCharacterList[person.getCharacter()] += 1
            
            if personCharacterList["altruist"] < personCharacterList["egoist"]:
                possible.remove("altruist")
            elif personCharacterList["altruist"] > personCharacterList["egoist"]:
                possible.remove("egoist")
            if personCharacterList["altruist"] < personCharacterList["hooligan"] and "altruist" in possible:
                possible.remove("altruist")
            elif personCharacterList["altruist"] > personCharacterList["hooligan"]:
                possible.remove("hooligan")
            if personCharacterList["hooligan"] < personCharacterList["egoist"] and "hooligan" in possible:
                possible.remove("hooligan")
            elif personCharacterList["hooligan"] > personCharacterList["egoist"] and "egoist" in possible:
                possible.remove("egoist")

            familyCharacter = choice(possible)

            self.character = familyCharacter
            return familyCharacter
        
        else:
            return self.character

    def getPerson(self):
        fam1 = ''  
        for member in self.personList:
            fam1 += self.personList[member].__str__() +"\n" 
        return fam1

    def getUpper(self):
        return self.apartment

    def getApartment(self):
        return self.apartment

    def getBlock(self):
        return self.apartment.getBlock()

    def getCity(self):
        return self.apartment.block.neighborhood.city

    def getType(self, sVal):
        if sVal == "up":
            return "a"
        elif sVal == "here":
            return "f"
        elif sVal == "down":
            return "p"

    def __str__(self):
        fam1 = ''  
        for member in self.personList:
            fam1 += member + " " + self.personList[member].__str__() + "\n" 
        return fam1 

# def main():
#     f1 = Family(1, "test")
#     print(f1.getPerson())
#     print(f1.getCharacter())

# if __name__ == "__main__": 
#     main()
