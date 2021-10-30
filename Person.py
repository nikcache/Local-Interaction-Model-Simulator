#Nikesh, Kunal and Abi
from random import randrange

class Person:

    def __init__ (self, character, social, member, familyKey):

        self.character = character
        self.social = social
        self.member = member
        self.family = familyKey
        self.friends = []
        self.payoff = 0
        self.nextRoundChar = ''
        self.i_payoff =  0
      
    

    def getPayoff(self): 
        return self.payoff

    def getiPayoff(self): 
        return self.i_payoff 
    
    def getFriends(self): 
        return self.friends
    
    def getCharacter(self):
        return self.character

    def getSocial(self):
        return self.social

    def getUpper(self):
        return self.family

    def getApartment(self):
        return self.family.getApartment()

    def getBlock(self):
        return self.family.getApartment().getBlock()

    def getType(self, sVal):
        if sVal == "up":
            return "f"
        elif sVal == "here":
            return "p"
    
    def setPayoff(self, payoff):  
        self.payoff = payoff

    def setiPayoff(self, payoff):  
        self.i_payoff = payoff

    def newChar(self): 
        self.character = self.nextRoundChar
        self.nextRoundChar = '' 
        self.payoff = 0 
    
    def setNextRoundChar(self, character): 
        self.nextRoundChar = character

    
    def friendLimit(self): 
        #print("Friend Length: ", len(self.friends))
        if (self.social == "introvert"):
            if (len(self.friends) >= 2):
                return False
        if (self.social == "extrovert"):
            if (len(self.friends) >= 7):
                return False
        return True 
    
    def linkFamily(self, family):
        self.family = family
    
    def createFriendLink(self, friend): 
        #if not self.friendLimit(): 
        self.friends.append(friend)
        #    return True 
        #return False 
        

    
    def __str__(self):
        return self.character + "-" + self.social +\
            " number of friends: "+ str(len(self.friends)) \
             +" payoff: "+str(self.payoff)+ "next round char: "+ self.nextRoundChar

def main(): 
    test1 = Person("altruist", "introvert", "father", 100)
    test2 = Person("altruist", "introvert", "son", 100)
    test3 = Person("altruist", "introvert", "son", 100)

    test1.createFriendLink(test2)
    test2.createFriendLink(test1)
    test1.createFriendLink(test3)
    print(test1.friends[0].getiPayoff())
    print(test2.friends)
    print(test1.friendLimit())
if __name__ == '__main__': 
    main() 