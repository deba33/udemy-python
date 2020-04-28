import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",  "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n"+card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in
        # from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        '''If total value > 21 and I still have an ace then change my ace to be 1 instead of 11.'''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# function for taking bets


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? \n"))
        except:
            print("Sorry! please provide an integer.")
        else:
            if chips.bet > chips.total:
                print(
                    f"Sorry, you don't have enough chips! you have: {chips.total}")
            else:
                break


# function for taking hits
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# function for prompting the player to hit or stand
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or stand? Enter h or s: ").lower()

        if x[0] == "h":
            hit(deck, hand)
        elif x[0] == "s":
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry! Please Enter h or s: ")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# functions to handle end of game scenarios
def player_busts(player, dealer, chips):
    print("Dealer WINS\nPlayer BUSTED")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS\nDealer BUSTED")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player WINS\nDealer BUSTED")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer WINS\nPlayer BUSTED")


def push(player, dealer):
    print("It's a tie ")


while True:

    print("WELCOME TO BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # show cards but keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f"\nPlayers total chips are at: {player_chips.total}")

    new_game = input("Would you like to play another hand? y/n: ").lower()

    if new_game[0] == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
