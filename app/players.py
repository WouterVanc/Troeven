from cards import Card


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.team: int | None = None
        self.cards: list[Card] = []

    def __str__(self) -> str:
        return (
            f"{self.name} is part of team {self.team} and currently holds {self.cards}"
        )

    def __repr__(self) -> str:
        return f"{self.name},{self.team},{self.cards}"

    def receive_cards(self, card: Card | list[Card]) -> None:
        match card:
            case Card():
                self.cards.append(card)
            case list():
                self.cards.extend(card)

    def play_card(self, card_idx: int) -> Card:
        return self.cards.pop(card_idx)


if __name__ == "__main__":

    from cards import Deck

    deck: Deck = Deck()
    deck.shuffle()
    print(deck)
    deck.lift_deck()
    print(deck)

    player_one: Player = Player(name="Wouter")

    print(player_one)

    player_one.receive_cards(card=deck.cards[:4])

    print(player_one)

    played_card: Card = player_one.play_card(card_idx=2)

    print(played_card)

    print(player_one)
