import random
class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for i in range(self.num_piles):
            print(f"{i}: ", end="")
            self.piles[i].print_all(i)

    def move(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        first_pile = self.piles[0]

        if p1 == 0 and p2 == 0:
            if first_pile.size() != 0:
                element =  first_pile.remove_top()
                first_pile.add_bottom(element)

        if p1 == 0 and p2 > 0:
            if first_pile.size() != 0:
                card1 = first_pile.peek_top()
                second_pile = self.piles[p2]
                if second_pile.size() != 0:
                    card2 = second_pile.peek_bottom()
                    if card1 == card2-1:
                        first_pile.remove_top()
                        second_pile.add_bottom(card1)
                else:
                    first_pile.remove_top()
                    second_pile.add_bottom(card1)

        if p1 > 0 and p2 > 0:
            if self.piles[p1].size() > 0 and self.piles[p2].size() > 0:
                card1 = self.piles[p1].peek_top()
                card2 = self.piles[p2].peek_bottom()
                if card1 == card2-1:
                    while self.piles[p1].size() > 0:
                        card = self.piles[p1].remove_top()
                        self.piles[p2].add_bottom(card)

    def is_complete(self):
        first_pile = self.piles[0]
        if first_pile.size() == 0:
            count = 0
            for values in self.piles:
                if values.size() != 0:
                    count += 1
            if count == 1:
                return True
        return False

    def pick_random(self):
        first_pile = self.piles[0]
        number = random.randint(1, self.num_cards)
        if number == 2:
            card = random.randint(1, 10)
            first_pile.add_top(card)
            print(f"Card number: {card} added to the top of pile 0!")

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.pick_random()
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end=": ")
            pile2 = int(input("Move to pile no.: "))
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            move_number += 1

        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")


class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        self.items.insert(0, item)

    def add_bottom(self, item):
        self.items.append(item)

    def remove_top(self):
        card = self.items[0]
        self.items.remove(card)
        return card

    def remove_bottom(self):
        card = self.items[-1]
        self.items.remove(card)
        return card

    def size(self):
        return len(self.items)

    def peek_top(self):
        return self.items[0]

    def peek_bottom(self):
        return self.items[-1]

    def print_all(self, index):
        if index != 0:
            string = ""
            card_list = self.items
            for cards in card_list:
                string += f"{cards} "
            print(string)
        else:
            string = ""
            if self.items != []:
                string = ""
                length = len(self.items) - 1
                string += str(self.items[0])
                string += " *" * length
            print(string)

cards = [3, 6, 2, 5, 4, 1]
game = Solitaire(cards)
game.play()