#create a uno game using the basic logical loops and OOP
# OOP is Object Oriented Programming

#first import the modules the we need

#this is for the random of the cards

import random

#we will use this in the time.sleep() for the executuion of the codes

import time

#this is for the players 1 and 2

player1 = input("Input player 1 name here: ")
player2 = input("Input player 2 name here: ")

# we set the variables we will use
# in the card type we will used the dictionary method because of key:value pairs

color = ("RED", "GREEN", "BLUE", "YELLOW")

rank = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw2", "Draw4", "Wild")

#we use the numbers and action as the definition of the dictionary

type = {"0":"number", "1":"number", "2":"number", "3":"number", "4":"number", "5":"number", "6":"number",
            "7":"number", "8":"number", "9":"number", "Skip":"action", "Reverse":"action", "Draw2":"action",
            "Draw4":"action_nocolor", "Wild":"action_nocolor"}

# this is for the object oriented programming part
# we use the OOP we will treat the variables as an object and objects have descriptions
# using the OOP model

# this is the OOP of the card

class Card: #the object should be capital because of the camel case

    #the __init__ is the syntax for the self
    def __init__(self, color, rank): #the parameters we can also use as variables

        self.rank = rank # this is the attribute of the parameter

        # we can also input if loops here

        if type[rank] == "number": #we set the type to number

            self.color = color #this will set the color

            self.cardtype = "number" #this will set the card type with number and color

        elif type[rank] == "action": #we set the type of action

            self.color = color #this will set the color

            self.cardtype = "action" #this will set the card type with the action

        else:

            self.color = None

            self.cardtype = "action_color"

    def __str__(self):

        if self.color == None: #this if the random is none of the above

            return self.rank

        else:

            return self.color + " " + self.rank #this will return  the outcome

# this is the OOP of the deck

class Deck:

    def __init__(self):

        self.deck = [] #this is an empty array

        for clr in color : #we use the for loop to declare the clr variable

            for ran in rank:

                if type[ran] != "action_nocolor":

                    self.deck.append(Card(clr, ran)) #the .append(Card(clr, ran)) will append the character color and rank

                    self.deck.append(Card(clr, ran))

                else:

                    self.deck.append(Card(clr, ran))

    def __str__(self):

        deck_comp = "" #this is the deck composition

        for card in self.deck: #use the for loop fir the variable of the card

            deck_comp += " " + card.__str__() #we use the += because it is increasing and looping

        return "The deck has " + deck_comp

    def shuffle(self):

        random.shuffle(self.deck) #this will shuffle the deck

    def deal(self): #we use deal as we give cards to the players

        return self.deck.pop() #we use the pop to remove the last card every draw

# this is for ht OOP of the hand

class Hand:

    def __init__(self):

        self.cards = [] #this is for the card

        self.cardsstr = [] #this is for the card in hand

        self.number_cards = 0 #this is the start of the number cards

        self.action_cards = 0 #this is the start of the action cards

    def add_card(self, card): #this for the adding of the card we use the parameter card

        self.cards.append(card) #this will add cards

        self.cardsstr.append(str(card)) #this will make the cards in hand as as tring

        if card.cardtype == "number":

            self.number_cards += 1

        else:

            self.action_cards += 1

    def remove_card(self, place): #this will remove your cards in hand

        self.cardsstr.pop(place - 1) #the parameter w use is palce to lay down card and use pop to remove card in hand

        return self.cards.pop(place - 1)

    def cards_in_hand(self): #this is for the card left in hand

        #we use the range function to have the length of the cards in hand
        for i in range(len(self.cardsstr)): #we use the for loops for the i variable

            print(f' {i + 1}.{self.cardsstr[i]}') #this will print the cards in increasing order

    def single_card(self, place): #this is for the single card in hand

        return self.cards[place - 1]

    def no_of_cards(self): #this is for the number of cards left

        return len(self.cards)

# this will randomly select who will start first

def choose_first(): #this is the function of the choose first

    if random.randint(0,1) == 0: # this is for the randomizer, if this is not in the global variable we can write it this way

        return player1

    else:

        return player2

# this is for the comparison if the cards placed by player 1 or 2 is valid with the latest card on top

def single_card_check(top_card, card):

    if card.color == top_card.color or top_card.rank == card.rank or card.cardtype == "action_nocolor":

        return True

    else:

        return False

# this is for the player 2 if valid card to lay down

def full_hand_check(hand, top_card):

    for c in hand.cards: # we use the c variable

        if c.color == top_card.color or c.rank == top_card.rank or c.cardtype == "action_nocolor":

            return hand.remove_card(hand.cardsstr.index(str(c)) + 1)

    else:

        return "no card"

# this will check if either cards will win

def win_check(hand):

    if len(hand.cards) == 0: #this is the logic the cards in hand is zero

        return True and print(player1 + " wins!")

    else:

        return False and print(player2 + " wins!")

# this will check if the last card placed is the action card (end game must be a number)

def last_card_check(hand):

    for c in hand.cards:

        if c.cardtype != "number": # this is the logic will check if the card type is a number or not

            return True

        else:

            return False

#this is the end of the OOP part of this project

#this is the start of the game loop

while True: # this will make the loop continuous

    print("\nWelcome to the UNO! players " + player1 + " and " + player2)

    deck = Deck() #the deck comes from the OOP that is why we set it to the variable deck

    deck.shuffle() #this will shuffle the deck from OOP

    player1_hand = Hand() #and again the Hand() comes form the Hand OOP, this is for player 1

    for i in range(7): #this is for the for loop with a variable of i, the range of 7 is the max of 7 cards in hand

        player1_hand.add_card(deck.deal()) #this will add card to the hand and the OOP of the deal() will give the card to the player

    player2_hand = Hand() #this is for the player 2 hand

    for i in range(7):

        player2_hand.add_card(deck.deal())

    top_card = deck.deal()

    if top_card.cardtype != "number": #this is the condition if the card type is not = to a number

        while top_card.cardtype != "number": #this is during the top card is not equal to a number

            top_card = deck.deal() #this will give the players the card from the deck

    print("\nStarting cards is: {}".format(top_card)) #this will print the card in hand, it is important to include the {} before the .format

    time.sleep(1) #this will delay the execution of the codes by 2 secs

    playing = True #this will make the loop continuous

    turn = choose_first() #this will make a decision who will go first

    print(turn + " will go first") #from the choose first function

    while playing: #this means that the game is running or meaning it is set to True

        if turn == player1:

            print("\nThe top card is " + str(top_card))
            print("This is your cards: ")

            player1_hand.cards_in_hand()

            if player1_hand.no_of_cards() == 1: #this is to check the number of cards in hand

                if last_card_check(player1_hand):

                    print("Last card cannot be action card \nadding one card to the deck")

                    player1_hand.add_card(deck.deal()) #the add_card() and .deal() is a function from th OOP above

                    print("Your Cards: ")

                    player1_hand.cards_in_hand()

            choice = input("\nPlace or Draw?(p/d): ") #this is an input from the player

            if choice == "p":

                pos = int(input("Enter the number of the card: "))

                temp_card = player1_hand.single_card(pos) #this is a temporary card

                if single_card_check(top_card, temp_card):

                    if temp_card.cardtype == "number":

                       top_card = player1_hand.remove_card(pos)

                       turn = player2

                    else:

                        if temp_card.rank == "Skip":

                            turn = player1

                            top_card = player1_hand.remove_card(pos)

                        elif temp_card.rank == "Reverse":

                            turn = player1

                            top_card = player1_hand.remove_card(pos)

                        elif temp_card.rank == "Draw2":

                            player2.add_card(deck.deal()) #this will draw 1

                            player2.add_card(deck.deal()) #this will draw another 1

                            top_card = player1_hand.remove_card(pos)

                            turn = player1

                        elif temp_card == "Draw4":

                            for i in range(4):

                                player1_hand.add_card(deck.deal())

                            top_card = player1_hand.remove_card(pos)

                            draw4color = input("Change color to 'in caps': ")

                            if draw4color != draw4color.upper():

                                draw4color = draw4color.upper()

                            top_card.color = draw4color

                            turn = player1

                else:
                    print("This is an invalid card!")

            elif choice == "d":

                temp_card = deck.deal()

                print("you drawn " + str(temp_card))

                time.sleep(1)

                if single_card_check(top_card, temp_card):

                    player1_hand.add_card(temp_card)

                else:

                    print("You cannot use this card")

                    player1_hand.add_card(temp_card)

                    turn = player2

            if win_check(player1_hand):

                print(player1 + " Wins!")

                playing = False

                break

        if turn == player2:

            if player2_hand.no_of_cards() == 1:

                if last_card_check(player2_hand):

                    time.sleep(1)

                    print("adding card to " + player2 + " hand")

                    player2.add_card(deck.deal())

            temp_card = full_hand_check(player2_hand, top_card)

            time.sleep(1)

            if temp_card != "no card":

                print(player2 + " throws: " + str(temp_card))

                time.sleep(1)

                if temp_card.cardtype == "number":

                    top_card = temp_card

                    turn = player1

                else:

                    if temp_card.rank == "Skip":

                        turn = player2

                        top_card = temp_card

                    elif temp_card.rank == "Reverse":

                        turn = player2

                        top_card = temp_card

                    elif temp_card.rank == "Draw2":

                        player1_hand.add_card(deck.deal())

                        player1_hand.add_card(deck.deal())

                        top_card = temp_card

                        turn = player2

                    elif temp_card.rank == "Draw4":

                        for i in range(4): #range of 4 because of 4 cards

                            player1_hand.add_card(deck.deal())

                        top_card = temp_card

                        draw4color = player2_hand.cards[0].color

                        print("The color change into ", draw4color)

                        top_card.color = draw4color

                        turn = player2

                    elif temp_card == "Wild":

                        top_card = temp_card

                        Wildcolor = player2_hand.cards[0].color

                        print("The color changes to", Wildcolor)

                        top_card.color = Wildcolor

                        turn = player1

            else:

                print("\nPulling a card from the deck")

                time.sleep(1)

                temp_card = deck.deal()

                if single_card_check(top_card, temp_card):

                    print(player2 + " throws " + str(temp_card))

                    time.sleep(1)

                    if temp_card.cardtype == "number":

                        top_card = temp_card

                        turn = player1

                    else:

                        if temp_card == "Skip":

                            turn = player2

                            top_card = temp_card

                        elif temp_card.rank == "Reverse":

                            turn = player2

                            top_card = temp_card

                        elif temp_card.rank == "Draw2":

                            player1_hand.add_card(deck.deal()) #for +1

                            player1_hand.add_card(deck.deal()) #repeat for another card drawn

                            top_card = temp_card

                            turn = player2

                        elif temp_card.rank == "Draw4":

                            for i in range(4):

                                player1_hand.add_card(deck.deal())

                            top_card = temp_card

                            draw4color = player2_hand.cards[0].color

                            print("The color changes into ", draw4color)

                            top_card.color = draw4color

                            turn = player2

                        elif temp_card.rank == "Wild":

                            top_card = temp_card

                            Wildcolor = player2_hand.cards[0].color

                            print("The color changes into ", Wildcolor)

                            top_card.color = Wildcolor

                            turn = player1

                else:

                    print(player2 + " does not have a card")

                    time.sleep(1)

                    player2_hand.add_card(temp_card)

                    turn = player1

                print(player2 + " has {} remaining cards ".format(player2_hand.no_of_cards()))

                time.sleep(1)

                if win_check(player2_hand):

                    print(player2 + " Wins!")

                    playing = False

    new_game = input("Another one? (y/n): ")

    if new_game == "y":

        continue

    else:

        print("Thank you for playing again!!")

        break

































































