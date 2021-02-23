import random

RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
SUITS = ['♠️', '♣️', '♥️', '♦️']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, ranks, suits):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)

    # TODO method to shuffle the deck
    # takes self and returns self with self.cards rearranged randomly
    def shuffle_deck(self):
        random.shuffle(self.cards)

    # TODO method to deal the top card of the deck to a player
    # takes a player and a deck and adds the top card from the deck to a player's hand
    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


class Game:
    def __init__(self, ranks, suits, name1, name2):
        self.deck = Deck(ranks, suits)
        self.deck.shuffle_deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.winner = False

    # TODO use deal_card() method from Deck class to deal 7 cards to each player
    def deal_hands(self):
        for _ in range(7):
            self.player1.hand.append(self.deck.deal_card())
            self.player2.hand.append(self.deck.deal_card())
        # print(self.player1.hand[0].suit)
        print("Hands dealt! Each player has 7 cards!")

    # TODO create turn action in which player asks for a card and goes fish according to the rules
    # Determine if the turn was a winning/losing turn


if __name__ == "__main__":

    g = Game(RANKS, SUITS, 'd', 'z')

    g.deal_hands()
