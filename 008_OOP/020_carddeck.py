#%% packages
import random

#%% class definition
class Deck:
    """Class for Card Deck

    """
    SUIT = ["♣", "♠", "♦", "♥"]  # unicode \u2660 - \u2663
    "\u2663"
    RANK = [str(n) for n in range(7, 11)] + ["J", "Q", "K", "A"]
    
    def __init__(self):
        self.cards = []
        for suit in self.SUIT:
            for rank in self.RANK:
                self.cards.append(f"{suit} {rank}")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def deal(self, num_hands, num_cards):
        self.hands = []
        for i in range(num_hands):
            self.hands.append([])
            for j in range(num_cards):
                self.hands[i].append(self.draw())
        return self.hands

    def __str__(self):
        return f"Deck of {self.cards}"

    def __repr__(self):
        print(f"Player Hands: {self.hands}")
        print(f"Deck: {self.cards}")
        return None

    def __len__(self):
        return len(self.cards)
    
    
    
#%% instantiate an object
deck = Deck()
deck.cards

# %%
deck.deal(num_cards=8, num_hands=2)

# %% repr and __str__
# __str__ invoked by print or str(object)
# str made for users
# return string object
# __repr__ invoked by repr and returns object in string format
# repr made for developers