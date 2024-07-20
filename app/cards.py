import random
from typing import Self


class Card:
    def __init__(self, suit: str, rank: int) -> None:
        self.suit: str = suit
        self.rank: int = rank

    def __str__(self) -> str:
        court_cards_map: dict[int, str] = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",
        }
        return f"{court_cards_map.get(self.rank, self.rank)} of {self.suit}"

    def __repr__(self) -> str:
        return f'({self.rank},"{self.suit}")'


class Deck:
    def __init__(self) -> None:
        suits: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks: list[int] = [i for i in range(9, 15)]

        self.cards: list[Card] = [
            Card(suit=suit, rank=rank) for suit in suits for rank in ranks
        ]

    def __str__(self) -> str:
        current_deck: list[str] = [str(card) for card in self.cards]
        return f"{current_deck}"

    def __repr__(self) -> str:
        return f"{self.cards}"

    def __iter__(self) -> Self:
        self.index = 0
        return self

    def __next__(self) -> Card:
        if self.index < len(self.cards):
            item: Card = self.cards[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def shuffle(self) -> None:
        random.shuffle(x=self.cards)

    def lift_deck(self) -> None:
        split_index: int = random.randint(a=0, b=23)
        self.cards: list[Card] = self.cards[split_index:] + self.cards[:split_index]


if __name__ == "__main__":

    hand = Card(suit="hearts", rank=12)

    print(hand)

    hand = Card(suit="hearts", rank=4)

    print(hand)

    deck = Deck()

    print(f"Unshuffled deck = {deck}")

    deck.shuffle()

    print(f"shuffled deck = {deck}")

    deck.lift_deck()

    print(f"lifted deck = {deck}")

    for card in deck:

        print(repr(card))
