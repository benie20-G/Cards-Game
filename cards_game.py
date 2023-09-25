from itertools import product
from random import shuffle
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

# cards = [(rank,suit) for suit in suits for rank in ranks]
cards = list(product(ranks,suits))
# for rank in ranks:
#     for suit in suits:
#         cards.append((rank, suit))
# print(cards)
# print(len(cards))
def shufflee(cards):
   shuffle(cards)
   return iter(cards)

card =shufflee(cards)
print(next(card))

def deal(cards, number_of_players):
    deck = shufflee(cards)

    deal_to_players(deck, number_of_players)
    deal_to_table(deck)

def get_players():
    while True:
        number_of_players= input("Enter thenumberof players you will use : ").strip()
        try:
            number_of_players =int(number_of_players)
        except:
            print("You have to provide a valid integer")
        else:
            if number_of_players in range(2,11):
                return number_of_players
            elif number_of_players<2:
                print("Atleast two players are needed")
            else:
                print(" use atmost 10 players")

def deal_to_players(cards,players):
    first_Cards = [next(cards) for _ in range(players())]
    second_Cards = [next(cards) for _ in range(players())]
    hands= zip(first_Cards,second_Cards)
    print()
    for i,(first_card,second_card) in enumerate(hands,start=1):
        print(f"player {i} was deal: {first_Cards},{second_card}")
        print()

def deal_to_table(deck):
    next(deck)
    flop = ','.join(str(next(deck)) for i in range(3))
    print(f'the flop: {flop}')
    next(deck)  # burn
    print(f"The turn: {next(deck)}")
    next(deck)  # burn
    print(f"The river: {next(deck)}")
    print()

deal(cards,get_players)