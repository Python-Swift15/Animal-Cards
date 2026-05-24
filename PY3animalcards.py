import random
import os

# =========================
# GAME DATA
# =========================

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

# =========================
# UTIL FUNCTIONS
# =========================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print("\n" + "=" * 40 + "\n")

def get_power(card):
    return ANIMAL_CARDS.index(card) + 1

def display_cards(cards):
    for i, card in enumerate(cards, start=1):
        print(f"{i}. {card} (Power {get_power(card)})")

# =========================
# GAME MODES
# =========================

def choose_mode():
    print("=== ANIMAL CARD BATTLE ===\n")
    print("1. Play vs Computer")
    print("2. Play vs Friend")

    choice = input("\nChoose mode (1 or 2): ")
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Pick 1 or 2: ")

    return choice == "1"  # True if vs computer

# =========================
# PLAYER INPUT (HIDDEN)
# =========================

def get_player_card(player_name, hand):
    clear_screen()

    print(f"=== {player_name}'s TURN ===\n")
    display_cards(hand)

    while True:
        try:
            choice = int(input("\nChoose a card number: "))
            if 1 <= choice <= len(hand):
                break
            else:
                print("Invalid number.")
        except:
            print("Enter a valid number.")

    card = hand.pop(choice - 1)

    input("\nPress ENTER to end your turn...")
    clear_screen()

    return card

# =========================
# AI
# =========================

def ai_choose_card(hand):
    best = max(hand, key=get_power)
    hand.remove(best)
    return best

# =========================
# FIGHT LOGIC
# =========================

def fight(card1, card2):
    print(f"{card1} vs {card2}!\n")

    # SPECIAL RULE
    if card1 == "Mouse" and card2 == "Elephant":
        print("Mouse defeats Elephant!")
        return 1
    if card2 == "Mouse" and card1 == "Elephant":
        print("Mouse defeats Elephant!")
        return 2

    p1 = get_power(card1)
    p2 = get_power(card2)

    if p1 > p2:
        print(f"{card1} wins!")
        return 1
    elif p2 > p1:
        print(f"{card2} wins!")
        return 2
    else:
        print("It's a draw!")
        return 0

# =========================
# MAIN GAME
# =========================

def start():
    vs_computer = choose_mode()

    player_score = 0
    opp_score = 0

    player_discard = []
    opp_discard = []

    player_deck = ANIMAL_CARDS * 5
    opp_deck = ANIMAL_CARDS * 5

    random.shuffle(player_deck)
    random.shuffle(opp_deck)

    # GAME LOOP
    while len(player_deck) >= 5:
        line()
        print(f"Cards remaining: {len(player_deck)}")

        player_hand = [player_deck.pop() for _ in range(5)]
        opp_hand = [opp_deck.pop() for _ in range(5)]

        # PLAYER 1
        card1 = get_player_card("Player 1", player_hand)

        # PLAYER 2 OR AI
        if vs_computer:
            card2 = ai_choose_card(opp_hand)
            print("AI has chosen a card...")
        else:
            input("Pass the device to Player 2 and press ENTER...")
            card2 = get_player_card("Player 2", opp_hand)

        # RESULT
        line()
        print("ROUND RESULT\n")
        print(f"Player 1 played: {card1}")
        print(f"{'AI' if vs_computer else 'Player 2'} played: {card2}\n")

        result = fight(card1, card2)

        if result == 1:
            player_score += 1
        elif result == 2:
            opp_score += 1

        # TRACK DISCARDS
        player_discard.append(card1)
        opp_discard.append(card2)

        # ROUND INFO
        print("\n--- Discarded Cards ---")
        print("Player 1:", player_discard)
        print(f"{'AI' if vs_computer else 'Player 2'}:", opp_discard)

        input("\nPress ENTER to continue...")

    # FINAL RESULTS
    clear_screen()
    line()
    print("FINAL RESULTS\n")
    print("Player 1 Score:", player_score)
    print(f"{'AI' if vs_computer else 'Player 2'} Score:", opp_score)

    if player_score > opp_score:
        print("\n Player 1 Wins!")
    elif player_score < opp_score:
        print(f"\n {'AI' if vs_computer else 'Player 2'} Wins!")
    else:
        print("\n It's a Tie!")

# RUN GAME
start()