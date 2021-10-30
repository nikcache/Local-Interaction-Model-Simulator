from Apartment import Apartment   
from random import choice
from Block import Block
from Neighborhood import Neighborhood
from City import City 
from math import inf 
from Family import Family

c = 0.5

def forceFriends(highestLevel, person): 
    for tempPerson in highestLevel.getPersonList():  
        if tempPerson.getSocial()=="extrovert" and tempPerson.friendLimit() and\
            tempPerson != person and tempPerson not in person.getFriends(): 
            return tempPerson
##        introvertList =[] 
##    for tempPerson in highestLevel.getPersonList():
##        if tempPerson.getSocial()=="introvert" and tempPerson.friendLimit() and\
##            tempPerson != person and tempPerson not in person.getFriends(): 
##            introvertList.append(tempPerson)
##        return choice(introvertList) 
        
def setLink(person, numFriends, highestLevel):  
    for i in range(5): 
        tempFriend = choice(highestLevel.getPersonList())
        if numFriends==0: 
            return person
        if tempFriend.friendLimit() and person.friendLimit() and tempFriend != person:
            person.createFriendLink(tempFriend)
            tempFriend.createFriendLink(person)
            numFriends-=1 
    while len(person.getFriends())<2 :
        if person.getCharacter()=="introvert": 
            for i in range(2): 
                forcedFriend = forceFriends(highestLevel, person)
                person.createFriendLink(forcedFriend)
                forcedFriend.createFriendLink(person)
        else: 
            for i in range(4): 
                forcedFriend = forceFriends(highestLevel, person)
                person.createFriendLink(forcedFriend)
                forcedFriend.createFriendLink(person)
            

    return person
        
def establishLinks(highestLevel):  
    for people in highestLevel.getPersonList():
        if people.social == "introvert": 
            setLink(people, 2, highestLevel)
        else: 
            setLink(people, 4, highestLevel)
    return highestLevel.getPersonList()

def payoffHelper(person):
    payoff = 0   
    for friend in person.getFriends(): 
        if friend.getCharacter()=="altruist":  
            payoff+=1
        elif friend.getCharacter()=="egoist": 
            pass
        elif friend.getCharacter()=="hooligan":  
            payoff-=c
    if person.getCharacter()=="altruist": 
        person.setPayoff(payoff-c) 
        person.setiPayoff(payoff-c)
    else:  
        person.setPayoff(payoff)
        person.setiPayoff(payoff)

def setPayoffIndividual(person): 
    payoff = 0 
    for friend in person.getFriends():  
        if friend.getCharacter()=="altruist":
            payoff += payoffHelper(friend)
    if person.getCharacter()=="altruist": 
        payoff-=c
        person.setPayoff(payoff) 
    else: 
        person.setPayoff(payoff)

def setPayOffRound(highestLevel):
    for person in highestLevel.getPersonList(): 
        payoffHelper(person)   

def avg(sum, n): 
    if n==0: 
        return -inf 
    else: 
        return sum/n
def nextRoundCharacter(person):
    hCount, aCount, eCount = 0, 0, 0
    hPayoff, aPayoff, ePayoff = 0, 0, 0
    people = []
    for f in person.getFriends():
        people.append(f)
    people.append(person)
    for friend in people: 
        if friend.getCharacter()=="altruist":
            aCount+=1 
            aPayoff+=friend.getPayoff()
        elif friend.getCharacter()=="egoist": 
            eCount+=1 
            ePayoff+=friend.getPayoff()
        else:  
            hCount+=1 
            hPayoff+=friend.getPayoff()
    aAvg, eAvg, hAvg = avg(aPayoff,aCount), avg(ePayoff,eCount), avg(hPayoff,hCount) 
    if aAvg > eAvg:
        if aAvg > hAvg: 
            return "altruist"
        elif aAvg == hAvg: 
            return choice (["altruist", "hooligan"])
        else:  
            return "hooligan"
    elif aAvg == eAvg:  
        if aAvg > hAvg: 
            return choice (["altruist", "egoist"])
        elif aAvg == hAvg:
            return choice (["altruist", "egoist", "hooligan"])
        else:  
            return "hooligan"
    else: #aAvg<eAvg
        if eAvg > hAvg: 
            return "egoist"
        elif eAvg == hAvg: 
            return choice (["egoist", "hooligan"]) 
        else: 
            return "hooligan"  


def setNextRoundChar(highestLevel):
    
    for person in highestLevel.getPersonList(): 

        person.setNextRoundChar(nextRoundCharacter(person))
    
    for person in highestLevel.getPersonList(): 
        person.newChar()
    

def percentageData(highestLevel): 
    aCount, eCount, hCount = 0, 0, 0
    total = 0 
    for person in highestLevel.getPersonList(): 
        if person.getCharacter() == "altruist": 
            aCount+=1
        elif person.getCharacter() == "egoist": 
            eCount+=1 
        else: 
            hCount+=1 
        total+=1
    return round(aCount/total*100, 1), round(eCount/total*100, 1), round(hCount/total*100, 1)
        
def main(): 
    block = City() 
    personList = establishLinks(block)
    print(percentageData(block))
    setPayOffRound(block)
    setNextRoundChar(block)
    
    print(percentageData(block))
    
    
    
if __name__ == "__main__": 
    main() 
