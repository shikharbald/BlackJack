# BlackJack Game
import time
import sys # system exit
import random
import plistlib
import re

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['Spades','Hearts','Clubs','Diamonds']

deck = []

for x in values:
    for y in suits:
        z = x+' '+y
        deck.insert(0,z)


def detValue(myList): # det the value of the card// ace situation still requires thought maybe two lists if ace?
    y = 0
    a = 0
    for x in myList:
        if (x=='K') or (x=='Q') or (x=='J'):
            myList.pop(y)
            #print(myList)
            #print("\n")
            myList.insert(y,10)
            #print(myList)
            #print("\n")
        y = y + 1
    y = 0
    for x in myList:
        if x=='A':
            myList.pop(y)
            myList.insert(y,11)
            z = 0
            for x in myList:
                z = z + int(x)
            if z > 21:
                myList.pop(y)
                myList.insert(y,1)
        a = a + 1
    return myList


# print function
def printDeck(myList):
    for x in myList:
        print(x)


def convList(myList): # Converts the list to a more basic version in order to help determine the value of cards.
    newList = []
    for x in myList:
        splitted = x.split()
        first = splitted[0]
       # print(first)
        #print("\n")
        second = splitted[1]
        #print(second)
       # print("\n")
        newList.insert(0,first)
        #print(newList)
        #print("\n")
    z = 0
    newList1 = detValue(newList)
    for y in newList1:
        z = z + int(y)
    return z



def bettervalue(newList, newList2):
    a = convList(newList)
    b = convList(newList2)
    if (a == b):
        print("tie")
    elif a > b:
        print("Dealer wins")
    elif a < b:
        print("You win")



def hit(newList, newList2):
        for card in deck[:1]:
            newList.insert(0, card)
        deck.pop(0)
        deck.pop(0)
        time.sleep(2)
        print(newList)
        print("Your new count is"+" "+str(convList(newList)))
        if convList(newList) > 21:
            time.sleep(2)
            print("You lose")
            print("Press r to restart or e to exit")
            userInput2 = str(input())
            if userInput2 == "r":
                game()
            elif userInput2 == "e":
                interface()
        elif convList(newList) == 21:
            print("BlacJack!!")
        elif convList(newList) < 21:
            print("Press H to hit or S to stand")
            userInput3 = str(input())
            if userInput3 == "H":
                time.sleep(2)
                print("\n")
                hit(newList,newList2)
            elif userInput3 == "S":
                stand(newList2, newList)


def stand(newList, newList2):
    for card in deck[:1]:
        newList.insert(0, card)
    deck.pop(0)
    deck.pop(0)
    a = convList(newList)
    time.sleep(2)
    print(newList)
    print("Dealer's count is"+" "+str(a))
    if a > 21:
        time.sleep(2)
        print("You win")
    elif a == 21:
        time.sleep(2)
        print("Dealer has blackjack you lose")
    elif 17 <= a < 21:
        time.sleep(2)
        bettervalue(newList, newList2)
    elif (a < 17):
        time.sleep(2)
        stand(newList, newList2)


def instructions():
    print("Press F to fold")
    print("Press H to hit")
    print("Hit R to return")
    userInput2 = str(input())
    if userInput2 == "R":
        interface()


def game():
    dealerList = []
    playerList = []
    random.shuffle(deck)
    #printDeck(deck)
    #print("\n")
    for card in deck[:2]:
        playerList.insert(0, card)
    #printDeck(playerList)
    #print("\n")
    deck.pop(0)
    #printDeck(deck)
    print("\n")
    deck.pop(0)
    #printDeck(deck)
    #print("\n")
    for card in deck[:1]:
        dealerList.insert(0, card)
    #printDeck(dealerList)
    #print("\n")
    z = convList(playerList) # contains the count of the card
    print(playerList)
    print("Your count is"+" "+str(z))
    y = convList(dealerList)
    print("\n")
    print(dealerList)
    print("Dealer's count is"+" "+str(y))
    print("\n")
    print("Press H to hit or S to stand")
    userInput = str(input())
    if userInput == "H":
        hit(playerList, dealerList)
    if userInput == "S":
        stand(dealerList, playerList)



def interface():
    print("Welcome to BlackJack")
    time.sleep(2)
    print("Press 1 for Instructions")
    print("Press 2 to play")
    print("Press 3 to quit")
    userInput = int(input())
    if userInput == 1:
        instructions()
    elif userInput == 2:
          game()
    elif userInput == 3:
        print("Goodbye")
    raise SystemExit


interface()


