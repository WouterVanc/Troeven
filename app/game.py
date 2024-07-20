from cards import Deck
from players import Player


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def decide_teams(self) -> None:
        deck: Deck = Deck()
        deck.shuffle()

        for i_card, card in enumerate(deck):
            print("##############")
            print(self.players[i_card % 4].name)
            print(card)
            print("##############")


if __name__ == "__main__":
    pass
