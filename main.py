import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self,new_deck=[]):
        self.cards = new_deck
    def draw_card(self):
        return self.cards.pop()
    def cards_left(self):
        return len(self.cards)
    def split_deeck(self):
        split_index = len(self.cards) // 2
        deck1 = Deck(self.cards[:split_index])
        deck2 = Deck(self.cards[split_index:])
        return deck1,deck2
    @classmethod
    def get_new_deck(cls):
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        original_deck = [Card(rank,suit) for suit in suits for rank in ranks]
        random.shuffle(original_deck)
        return cls(original_deck)
class Player:
    def __init__(self,deck):
        self.deck = deck
        self.discardet = []
class Game:
    def __init__(self):
        full = Deck.get_new_deck()
        d1,d2 = full.split_deeck()
        self.player1 = Player(d1)
        self.player2 = Player(d2)
        self.player1_curent = []
        self.player2_curent = []
    
    
def main():
    
    full = Deck.get_new_deck()
    d1,d2 = full.split_deeck()
    print("full deck:")
    for card in d1.cards:
        print(card)
    print("full deck2:")
    for card in d2.cards:
        print(card)

if __name__ == "__main__":
    main()