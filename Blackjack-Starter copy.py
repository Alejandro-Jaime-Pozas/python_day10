# for the game, there are multiple objects (classes):
#     1 player
#     1 dealer
#     1 deck of cards
#     1 game to play (like the Blog class)
    
# once backend complete, start playing
# ========================================================================================================

from IPython.display import clear_output
import random, time
    
# deck of cards is made up of 52 unique cards which are shuffled. can create card class, 
#     then deck class? 
#     a card class would basically only create a card object, the deck class would take all 52 card instances, then shuffle.
#     maybe shuffle only when playing the game? so in the game class?

# create 4 suits list, 13 cards per suit
# create 13 card dict w key and value for that card number

suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
cards = {'Ace':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
# need to create for loop to create a deck with suits * cards, then a dict wth k, v pairs to assing value.


# CARD CLASS===================================================================================================
# create a class which creates a unique card object
class Card:
    # a card object should only have characteristics, no methods..its properties are having a suit, name, and value.
    # once the card has those properties in it, i can pass them through a deck to create unique deck of cards
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name} of {self.suit}"
    
    def __repr__(self):
        return f"<{self.name} of {self.suit} card_obj>"

# DECK CLASS=====================================================================================================
# create a class for deck which loops through suits and cards to create 52 unique card objects contained within deck inst.
class Deck:
    def __init__(self):
        self.new_deck = []
        
    def create_deck(self, ):
        for suit in suits:
            for name, value in cards.items():
                new_card = Card(suit, name, value)
                self.new_deck.append(new_card)
        return self.new_deck
            
    def __str__(self):
        return f"this is a deck instance."
    
# PLAYER CLASS=========================================================================================================
# player and dealer both take cards from deck, and can hit, stand, w some differences like
#     player can place bets and has limited chips, can choose to hit or stand when <= 21
#     dealer has to hit if < 17, can only turn their hidden card when player stands or busts

# unique qualities of player instance: starting chips, name, hand?, 
# unique methods for player instance: hit, stand, bet, +/- chip balance
class Player:    
    def __init__(self, name, chips, ):
        self.name = name
        self.chips = chips
        self.hand = []
    
    def __str__(self):
        return f"Player name: {self.name}, player chips: {self.chips}"
    
    def __repr__(self):
        return f"<Player name: {self.name}, player chips: {self.chips}>"

        
# DEALER CLASS==========================================================================================================

class Dealer:
    def __init__(self):
        self.hand = []
        
        

# GAME CLASS============================================================================================================== 
# game to play contains the backend of the game, 
        # GAME modify player chip count based on bet
        # GAME create a new deck, shuffle the deck
        # GAME deal player 1 card, dealer 1 card, player other card, dealer other card from deck
        # GAME show player their hand, dealers hand w one hidden card
        # if choice == 'h':
        #             pass # GAME while loop until player busts or stands
        # GAME show both dealer cards including hidden card
        # GAME - while dealer hand < 17 and player not busted, dealer hits, add card to dealer hand
        # GAME if/else to check if player wins, loses, or pushes
        
#     GAME END RESULT - while dealer hand < 17 and player not busted, dealer hits, add card to dealer hand
#     GAME END RESULT - if dealer hand > 16, dealer stands, end dealer turn
#     GAME END RESULT - if player hand > dealer hand, player wins
#         return player bet * 2
#     GAME END RESULT - if player hand = dealer hand, push
#         return player bet
#     GAME END RESULT - if player hand < dealer hand, player loses
#     GAME END RESULT - end round, ask player if want to play again
    
class Game():
#     for the game part, events include: 
#         reducing player chip count by bet amount, 
#         adding cards from deck to player hand to start
#         adding cards from deck to dealer hand to start
#         adding cards from deck to player hand IF PLAYER HITS
#         adding cards from deck to dealer hand IF DEALER < 17
#         deciding if player wins or loses round
#         changing player chip count if win or loss
        
        
#     so, Game init for now should have nothing, b/c all updates will be made to the player, dealer, decks classes
#     so, do i need a general game fn? one which calls other game fns? maybe yes. or no
#     I DO NOT NEED A GENERAL GAME FN. just individual fns which are called from the play_blackjack

    def create_shuffled_deck(self):
        shuffled_deck = Deck()
        shuffled_deck = shuffled_deck.create_deck()
        random.shuffle(shuffled_deck)
#         print(shuffled_deck)
        
    def bet_amount(self, bet):
        print(p1.name)
        
    

# to run the game, need main fn with while loops, inputs, class instances, fn calls that occur
#     while playing the game, such as if blackjack, then payout is 1.5x

def play_blackjack():
    
    play = True
    
    while play:
        # ask player name
        g1 = Game()
        name = input('What is your name: ')
        p1 = Player(name, 100)
        print(f"\nLet's play blackjack {p1.name.title()}!\n")
        print(p1)
        bet = int(input(f'\nHow much do you want to bet? ({p1.chips} available): '))
        while bet not in range(1, p1.chips + 1):
            print(p1.chips)
            bet = int(input("That's either too much or too little. How much do you want to bet: "))
        # GAME modify player chip count based on bet
        g1.bet_amount(bet)
        # GAME create a new deck, shuffle the deck
        g1.create_shuffled_deck()
        # GAME deal player 1 card, dealer 1 card, player other card, dealer other card from deck
        # GAME show player their hand, dealers hand w one hidden card
        choice = input("Hit or Stand (h/s): ").lower()
        while choice not in {'h', 's'}:
            choice = input("Sorry, do you want to Hit or Stand (h/s): ").lower()
        if choice == 'h':
            pass # GAME while loop until player busts or stands
        elif choice == 's':
            pass
        # GAME show both dealer cards including hidden card
        # GAME - while dealer hand < 17 and player not busted, dealer hits, add card to dealer hand
        # GAME if/else to check if player wins, loses, or pushes
        
        
        break

    
play_blackjack()