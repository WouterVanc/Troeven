from cards import Card


class Player:

    def __init__(self, name: str, cards: list[Card], team: int) -> None:
        self.name: str = name
        self.cards: list[Card] = cards
        self.team: int = team

    def __str__(self) -> str:
        return (
            f"{self.name} is part of team {self.team} and currently holds {self.cards}"
        )

    def play_card(self, card: Card) -> None:
        self.cards.remove(card)


if __name__ == "__main__":

    cards: list[Card] = [
        Card(suit="Hearts", rank=12),
        Card(suit="Spades", rank=10),
        Card(suit="Diamonds", rank=9),
        Card(suit="Clubs", rank=2),
    ]

    player_one: Player = Player(name="wouter", cards=cards, team=1)

    print(player_one)

    player_one.play_card(card=cards[0])

    print(player_one)
