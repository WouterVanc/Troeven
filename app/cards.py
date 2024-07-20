import random


class Card:
    def __init__(self, suit: str, rank: int) -> None:
        self.suit: str = suit
        self.rank: int = rank

    def __repr__(self) -> str:
        court_cards_map: dict[int, str] = {
            11: "jack",
            12: "queen",
            13: "king",
            14: "ace",
        }
        return f"{court_cards_map.get(self.rank, self.rank)} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        suits: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks: list[int] = [i for i in range(9, 15)]

        self.cards: list[Card] = [
            Card(suit=suit, rank=rank) for suit in suits for rank in ranks
        ]

    def __str__(self) -> str:
        return f"{self.cards}"

    def shuffle(self) -> None:
        random.shuffle(x=self.cards)


if __name__ == "__main__":

    hand = Card(suit="hearts", rank=12)

    print(hand)

    hand = Card(suit="hearts", rank=4)

    print(hand)

    deck = Deck()

    print(f"Unshuffled deck = {deck}")

    deck.shuffle()

    print(f"shuffled deck = {deck}")
