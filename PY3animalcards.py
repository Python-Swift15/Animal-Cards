import random

# Power ranking (weakest → strongest)
ANIMAL_CARDS = [
    "Mouse",
    "Chicken",
    "Goat",
    "Wolf",
    "Buffalo",
    "Tiger",
    "Lion",
    "Elephant"
]


# Get power of a card
def get_power(card):
    return ANIMAL_CARDS.index(card) + 1


# Display cards nicely
def display_cards(cards):
    for i, card in enumerate(cards, start=1):
        print(f"{i}. {card} - Power: {get_power(card)}")


# Fight function
def fight(card1, card2):
    print(f"{card1} is fighting {card2}!")

    power1 = get_power(card1)
    power2 = get_power(card2)

    if power1 > power2:
        print(f"{card1} has defeated {card2}!!!")
        return 1
    elif power2 > power1:
        print(f"{card2} has defeated {card1}!!!")
        return 2
    else:
        print("It's a draw!")
        return 0


def start():
    # Create decks
    player_deck = ANIMAL_CARDS.copy()
    opp_deck = ANIMAL_CARDS.copy()

    random.shuffle(player_deck)
    random.shuffle(opp_deck)

    print("=== Animal Cards Game ===\n")

    # Game loop
    while len(player_deck) > 0 and len(opp_deck) > 0:

        print("\nCards in the opponent's deck:")
        display_cards(opp_deck)

        # AI chooses (last card)
        opp_card = opp_deck.pop()
        print(f"\nThe opponent has chosen {opp_card}.\n")

        print("Cards in your deck:")
        display_cards(player_deck)

        # Player chooses
        while True:
            try:
                choice = int(input("Choose a card to play (type the number): "))
                if 1 <= choice <= len(player_deck):
                    break
                else:
                    print("Invalid number, try again.")
            except:
                print("Please enter a valid number.")

        player_card = player_deck.pop(choice - 1)

        print(f"\nYou have chosen {player_card}.\n")

        # Fight!
        fight(player_card, opp_card)

    print("\n=== The battle has ended! ===")


# Run game
start()