from random import shuffle

def create_deck():
    deck = []

    face_values = ["A", "J", "Q", "K"]
    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))

        for card in face_values:
            deck.append(card)

    shuffle(deck)
    return deck