from deck import Deck
class PokerHand:
    """
    class representing a poker hand
    we will work to ran k the hand and determine trips, full house, 4 of a kind, etc
    """
    def __init__(self):
        deck = Deck()
        deck.shuffle()
        _cards = []
        for i in range(5):
            _cards.append(deck.deal())
            self._cards = _cards

    def __str__(self):
        return str(self._cards)

hand = PokerHand
print(hand)

