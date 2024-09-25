import random

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation for str()."""
        return f'{str(self):{format}}'


class DeckOfCards:
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13],
                                   Card.SUITS[count // 13]))

    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except IndexError:
            return None

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        return s


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw_card(self, deck, card_number):
        if 1 <= card_number <= 52:
            card_index = card_number - 1 
            if card_index < len(deck._deck):
                card = deck._deck.pop(card_index)
                self.hand.append(card)
                return card
            else:
                print(f"Card number {card_number} is already drawn.")
                return None
        else:
            print("Please enter a number between 1 and 52.")
            return None

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)


# tow players
player1 = Player('Ghassan')
player2 = Player('pl')

# create cards and shuffle them
deck = DeckOfCards()
deck.shuffle()

 #player chose a card 
chosen_number1 = int(input(f"{player1.name}, choose a card nomber (1-52): "))
chosen_card1 = player1.draw_card(deck, chosen_number1)
print(f"{player1.name} played this {chosen_card1}")

chosen_number2 = int(input(f"{player2.name}, choose a cad number betwwen (1-52): "))
chosen_card2 = player2.draw_card(deck, chosen_number2)
print(f"{player2.name} played this {chosen_card2}")

#display card of player
print(f"{player1.name}'s card: {player1.show_hand()}")
print(f"{player2.name}'s card: {player2.show_hand()}")
    