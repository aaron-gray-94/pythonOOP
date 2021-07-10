class Card:
    def __init__(self, suit, val, pip):
        self.suit = suit
        self.val = val
        self.pip = pip

    def showCard(self):
        print(f"{self.pip} of {self.suit}, with val {self.val}")

class Deck:

    def __init__(self, numCards):
        self.numCards = numCards
        self.cards = []
        self.reset()
    
    def reset(self):
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        pips = [ None, "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        for suit in suits:
            for val in range(1, len(pips)):
                self.cards.append(Card(suit, val, pips[val]))

    def showDeck(self):
        for card in self.cards:
            card.showCard()

    def shuffleDeck(self):
        for i in range(self.numCards-1,1,-1):
            j = randint(1,self.numCards-1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        return self.cards

mydeck = Deck(52)
mydeck.showDeck()
mydeck.shuffleDeck()

# myname = input("Please type your name:")
# print(myname)