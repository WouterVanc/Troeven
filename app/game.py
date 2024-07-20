from cards import Card, Deck
from players import Player


class Game:

    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def decide_teams(self) -> None:
        deck: Deck = Deck()
        deck.shuffle()

        for i_card, card in enumerate(deck):
            print(self.players[i_card % 4].name)
            print(card)
            print("##############")


if __name__ == "__main__":

    play1 = Player(
        name="wouter",
        cards=[
            Card(suit="Diamonds", rank=3),
            Card(suit="Hearts", rank=7),
            Card(suit="Spades", rank=5),
            Card(suit="Clubs", rank=11),
        ],
    )
    play2 = Player(
        name="alice",
        cards=[
            Card(suit="Spades", rank=13),
            Card(suit="Clubs", rank=4),
            Card(suit="Hearts", rank=1),
            Card(suit="Diamonds", rank=8),
        ],
    )
    play3 = Player(
        name="bob",
        cards=[
            Card(suit="Clubs", rank=10),
            Card(suit="Diamonds", rank=6),
            Card(suit="Spades", rank=2),
            Card(suit="Hearts", rank=11),
        ],
    )
    play4 = Player(
        name="charlie",
        cards=[
            Card(suit="Hearts", rank=3),
            Card(suit="Clubs", rank=8),
            Card(suit="Diamonds", rank=12),
            Card(suit="Spades", rank=7),
        ],
    )

    players: list[Player] = [play1, play2, play3, play4]

    test_game: Game = Game(players=players)

    test_game.decide_teams()
