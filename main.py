import random
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
class Card:
    def __init__(self,rank,suit):
        self._rank = rank
        self._suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    @property
    def rank(self):
        return self._rank
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self,new_suit):
        self._suit =  new_suit
    @rank.setter
    def rank(self,new_rank):
        self._rank = new_rank
    
class Deck:
    def __init__(self,new_deck=[]):
        self._cards = new_deck
    @property
    def cards(self):
        return self._cards
    @cards.setter
    def cards(self, new_deck):
        self._cards = new_deck
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
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        original_deck = [Card(rank,suit) for suit in suits for rank in card_ranks]
        random.shuffle(original_deck)
        return cls(original_deck)
class Player:
    def __init__(self,deck):
        self.deck = Deck(deck)
        self.discardet = Deck()
class Game:
    def __init__(self):
        full = Deck.get_new_deck()
        d1,d2 = full.split_deeck()
        self.player1 = Player(d1.cards)
        self.player2 = Player(d2.cards)
        self.player1_curent = []
        self.player2_curent = []
    def battle(self):
        card1 = self.player1.deck.draw_card()
        card2 = self.player2.deck.draw_card()
        if card_ranks.index(card1.rank) == card_ranks.index(card2.rank):
            self.war()
        elif card_ranks.index(card1.rank) > card_ranks.index(card2.rank):
            self.player1.discardet.cards.extend([card1,card2]) 
        elif card_ranks.index(card1.rank) < card_ranks.index(card2.rank):
    def war(self):
        ...
    def __str__(self):
        card_list = ''
        card_list2 = ''
        for card in self.player2.discardet.cards[:2]:
            card_list = card_list + '/n' + card.rank + ' ' + card.suit
        for card in self.player2.deck.cards[:2]:
            card_list2 = card_list2 + '/n' + card.rank + ' ' + card.suit
        return  card_list + ' ------ ' + card_list2
    
    
def main():
    game = Game()
    game.battle()
    print(game)

if __name__ == "__main__":
    main()