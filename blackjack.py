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

class Player:

    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0

    def __str__(self):
        current_hand = ""

        for card in self.hand:
            current_hand += str(card) + " "

        final_status = current_hand + "score: " + str(self.score)

        return final_status

def set_score(self):
    self.score = 0

    face_cards_dict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                        "7": 7, "8": 8, "9": 9, "10": 10}
    ace_counter = 0

    for card in self.hand:
        self.score += face_cards_dict[card]
        if card == "A":
            ace_counter += 1
        if self.score > 21 and ace_counter != 0:
            self.score -= 10
            ace_counter -= 1

    return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result:
            if self.score == 21 and len(self.hand) === 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2 * self.bet

            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def has_blackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False


def print_house(house):
    for card in range(len(house.hand)):  # e.g if len(House.hand) = 5
        # range will be 0,1,2,3,4
        if card == 0:  # first card
            print("X", end = " ")  # end=" " keeps printing on the same line
        elif card == len(house.hand[card]) - 1:  #last card
            print(house.hand[card]) # prints last card
        else:
            print(house.hand[card])
       

card_deck = create_deck()

first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]
player1 = Player(first_hand)
house = PLayer(second_hand)

while True:
    if len(card_deck) < 20:
        card_deck = create_deck()  #brand new card deck
    
    first_hand = [card_deck.pop(), card_deck.pop()]
    second_hand = [card_deck.pop(), card_deck.pop()]
    player1.play(first_hand)
    house.play(second_hand)

    bet = int(input("Please enter your bet: "))
    player1.bet_money(bet)
    print_house(house)
    print(player1)

    if player1.has_blackjack():
        if house.has_blackjack():
            player1.draw()
        else:
            player1.win(True)

    else:
        while player1.score < 21:
            action = input("Do you want another card? (y/n): ")
            if action == "y":
                player1.hit(card_deck.pop())
                print(player1)
                print_house(house)
            else:
                break
        while house.score > 21:
            print(house)
            house.hit(card_deck.pop())

        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(False)

        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                player1.win(False)

    
    print(player1.money)
    print(house)

# you can add a list of players in an array
# use a for in loop to go through it